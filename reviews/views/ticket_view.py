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
    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Create a form instance with the submitted data and files
        form = TicketForm(request.POST, request.FILES)

        # Check if the form data is valid
        if form.is_valid():
            # Create a Ticket object but don't save it to the database yet
            ticket = form.save(commit=False)

            # Assign the currently logged-in user to the ticket
            ticket.user = request.user

            # Save the ticket to the database
            ticket.save()

            # Redirect the user to the feed page after saving
            return redirect("feed")
    else:
        # If the request is GET, create an empty form
        form = TicketForm()

    # Render the ticket template with the form
    return render(request, "reviews/ticket.html", {
        "form": form,      # Pass the form to the template
        "mode": "create",  # Tell the template we are in 'create' mode
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