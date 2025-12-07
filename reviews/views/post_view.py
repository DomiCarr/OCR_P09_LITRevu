from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Ticket

@login_required
def post_view(request):
    """
    Returns all posts (tickets and reviews) created by the logged-in user.
    Reviews include the linked ticket.
    """
    # User's own reviews
    reviews = Review.objects.filter(user=request.user).order_by('-time_created')\
        .annotate(content_type=Value('REVIEW', CharField()))

    # User's own tickets
    tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')\
        .annotate(content_type=Value('TICKET', CharField()))

    # Merge and sort by creation date
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'reviews/post.html', context={'posts': posts})
