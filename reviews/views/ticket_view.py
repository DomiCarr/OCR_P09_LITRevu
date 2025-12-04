# reviews/views/ticket_view.py
from django.shortcuts import render, redirect, get_object_or_404
from reviews.forms.ticket_form import TicketForm
from reviews.models import Ticket


# -------------------------------------------------------------------
# Create ticket view
# -------------------------------------------------------------------
def create_ticket(request):
    """
    Handles ticket creation.
    GET: display empty form
    POST: validate form, assign current user, save, redirect
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("feed")
    else:
        form = TicketForm()

    return render(request, "reviews/ticket.html", {
        "form": form,
        "mode": "create",
    })


def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = TicketForm(instance=ticket)

    return render(request, "reviews/ticket.html", {
        "form": form,
        "ticket": ticket,
        "edit_mode": True,  # booléen pour template
    })