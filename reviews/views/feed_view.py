# reviews/views/feed_view.py
from itertools import chain
from django.db.models import CharField, Value, Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Ticket, UserFollows


def get_users_reviews(user):
    """
    Retourne les reviews que l'utilisateur peut voir :
    - ses propres reviews
    - les reviews des utilisateurs suivis
    - les reviews en réponse à ses tickets
    """
    followed_users_ids = UserFollows.objects.filter(
        user=user
    ).values_list('followed_user', flat=True)

    reviews = Review.objects.filter(
        Q(user__id__in=followed_users_ids) |
        Q(user=user) |
        Q(ticket__user=user)
    ).order_by('-time_created')

    return reviews.annotate(content_type=Value('REVIEW', CharField()))


def get_users_tickets(user):
    """
    Retourne les tickets que l'utilisateur peut voir :
    - ses propres tickets
    - tickets des utilisateurs suivis
    """
    followed_users_ids = UserFollows.objects.filter(
        user=user
    ).values_list('followed_user', flat=True)

    tickets = Ticket.objects.filter(
        Q(user__id__in=followed_users_ids) | Q(user=user)
    ).order_by('-time_created')

    return tickets.annotate(content_type=Value('TICKET', CharField()))


@login_required
def feed_view(request):
    reviews = get_users_reviews(request.user)
    tickets = get_users_tickets(request.user)

    # Fusionne et trie par date de création
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'reviews/feed.html', context={'posts': posts})
