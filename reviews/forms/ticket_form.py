from django import forms
from reviews.models import Ticket

class TicketForm(forms.ModelForm):
    """Form used to create or edit a ticket."""

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "input"}),
            "description": forms.Textarea(attrs={"class": "textarea"}),
        }
