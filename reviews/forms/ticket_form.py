from django import forms
from reviews.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'description': forms.Textarea(attrs={'id': 'description'}),
            'image': forms.FileInput(attrs={'id': 'id_image', 'style': 'display:none;'}),
        }
