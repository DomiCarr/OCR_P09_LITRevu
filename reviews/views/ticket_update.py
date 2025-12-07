# reviews/views/ticket_update.py
from django.shortcuts import get_object_or_404, redirect, render
from reviews.models import Ticket
from reviews.forms.ticket_form import TicketForm
from django.contrib.auth.decorators import login_required

@login_required
def ticket_update(request, ticket_id):
    """Edit a ticket created by the logged-in user."""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'reviews/ticket_create.html', {'ticket_form': form})
