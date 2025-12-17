# reviews/views/feed_view.py
from itertools import chain
from django.db.models import CharField, Value, Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Ticket, UserFollows


def get_users_tickets(user):
    """
    Returns tickets the user can see:
    - user's own tickets
    - tickets from followed users
    - excludes tickets that already have at least one review
    """
    # Filter UserFollows table for all rows where the follower
    # is the given user
    # This returns a queryset of UserFollows objects
    user_follows_qs = UserFollows.objects.filter(user=user)

    # Extract the 'followed_user' field values as a flat list of IDs
    # flat=True converts the queryset
    # to a simple list instead of a list of tuples
    followed_users_ids = (
        user_follows_qs
        .values_list('followed_user', flat=True)
        )

    # Combine the list of followed user IDs with the current user's ID
    # list(followed_users_ids) converts the queryset to a Python list
    # [user.id] adds the current user's own ID so their tickets are included
    user_and_followed_ids = list(followed_users_ids) + [user.id]

    # Query the Ticket table for tickets authored by the user or followed users
    tickets_qs = Ticket.objects.filter(user__in=user_and_followed_ids)

    # Exclude tickets that already have at least one associated review
    # review__isnull=False checks if the reverse ForeignKey from Review exists
    tickets_qs = tickets_qs.exclude(review__isnull=False)

    # Return the final queryset of tickets
    return tickets_qs


def get_users_reviews(user):
    """
    Returns reviews the user can see:
    - user's own reviews
    - reviews from followed users
    - reviews in response to user's tickets
    """
    followed_users_ids = UserFollows.objects.filter(
        user=user
    ).values_list('followed_user', flat=True)

    reviews = Review.objects.filter(
        Q(user__id__in=followed_users_ids) |
        Q(user=user) |
        Q(ticket__user=user)
    ).order_by('-time_created')

    # Annotate each review with a content type
    return reviews.annotate(content_type=Value('REVIEW', CharField()))


@login_required
def feed_view(request):
    """
    Renders the feed page:
    - combines reviews and tickets
    - sorts by creation date (most recent first)
    """
    reviews = get_users_reviews(request.user)
    tickets = get_users_tickets(request.user)

    # Merge the querysets and sort by time_created
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'reviews/feed.html', context={'posts': posts})
