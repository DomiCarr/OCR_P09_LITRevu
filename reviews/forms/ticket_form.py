from django import forms
from reviews.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'description': forms.Textarea(attrs={'id': 'description'}),
            'image': forms.FileInput(attrs={'id': 'image'})
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Une image est obligatoire.")
        return image
