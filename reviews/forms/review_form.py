# reviews/forms/review_form.py
from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    NOTE_CHOICES = [(i, str(i)) for i in range(6)]  # 0 à 5

    note = forms.ChoiceField(
        choices=NOTE_CHOICES,
        widget=forms.RadioSelect(attrs={'id': 'note'}),
        label="Note"
    )

    class Meta:
        model = Review
        fields = ['titre', 'note', 'commentaire']
        widgets = {
            'titre': forms.TextInput(attrs={'id': 'titre'}),
            'commentaire': forms.Textarea(attrs={'id': 'commentaire'}),
        }
