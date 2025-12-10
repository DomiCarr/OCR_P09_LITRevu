# reviews/views/ticket_update.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from reviews.models import Ticket
from reviews.forms.ticket_form import TicketForm


@login_required
def ticket_update(request, ticket_id):
    """Edit a ticket created by the logged-in user."""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('post')  # redirige vers la page posts
    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        'reviews/ticket.html',         # <- on utilise ton template existant
        {
            'form': form,               # <- nom attendu par le template
            'edit_mode': True,          # <- pour afficher "Modifier"
            'ticket': ticket            # <- pour l'image preview
        }
    )
