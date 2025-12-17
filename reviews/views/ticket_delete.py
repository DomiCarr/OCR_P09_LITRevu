# reviews/views/ticket_delete.py
from django.shortcuts import get_object_or_404, redirect
from reviews.models import Ticket
from django.contrib.auth.decorators import login_required


@login_required
def ticket_delete(request, ticket_id):
    """Delete a ticket created by the logged-in user."""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    ticket.delete()
    return redirect('post')
