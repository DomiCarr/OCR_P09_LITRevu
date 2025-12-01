# reviews/forms/auth_forms.py
from django import forms
from django.contrib.auth.models import User


# -------------------------------------------------------------------
# SignupForm: handles user registration
# -------------------------------------------------------------------
class SignupForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmer le mot de passe",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        help_texts = {
            'username': '',  # Remove Django default help text
        }

    # Custom validation to ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")


# -------------------------------------------------------------------
# LoginForm: handles user login
# -------------------------------------------------------------------
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)


