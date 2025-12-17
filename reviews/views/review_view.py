# reviews/views/review_view.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reviews.models import Ticket
from reviews.forms.ticket_form import TicketForm
from reviews.forms.review_form import ReviewForm


@login_required
def create_review(request, ticket_id=None):
    """
    Create a review. Two modes:
    - if ticket_id provided -> post a review on existing ticket
    - if no ticket_id -> create ticket then review
    """
    ticket = None
    ticket_form = None

    # Mode: response to existing ticket
    if ticket_id is not None:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if request.method == "POST":
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.ticket = ticket
                review.user = request.user
                review.save()
                return redirect("feed")
        else:
            review_form = ReviewForm()

        return render(
            request,
            "reviews/review_create.html",
            {"ticket": ticket, "review_form": review_form},
        )

    # Mode: create ticket + review in same form
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect("feed")
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request,
        "reviews/review_create.html",
        {
            "ticket": None,
            "ticket_form": ticket_form,
            "review_form": review_form,
        },
    )
