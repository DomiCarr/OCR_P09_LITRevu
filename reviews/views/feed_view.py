# reviews/views/feed_view.py
from itertools import chain
from django.db.models import CharField, Value, Q, Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Ticket, UserFollows


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


def get_users_tickets(user):
    """
    Returns tickets the user can see:
    - user's own tickets
    - tickets from followed users
    - excludes tickets that already have at least one review
    """
    followed_users_ids = UserFollows.objects.filter(
        user=user
    ).values_list('followed_user', flat=True)

    tickets = Ticket.objects.annotate(
        reviews_count=Count('review')  # count reviews for each ticket
    ).filter(
        (Q(user__id__in=followed_users_ids) | Q(user=user)) &
        Q(reviews_count=0)  # only tickets with no reviews
    ).order_by('-time_created')

    # Annotate each ticket with a content type
    return tickets.annotate(content_type=Value('TICKET', CharField()))


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
