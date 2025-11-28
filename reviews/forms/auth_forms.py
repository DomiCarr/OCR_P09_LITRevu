# reviews/forms/auth_forms.py
from django import forms
from django.contrib.auth.models import User


# -------------------------------------------------------------------
# SignupForm: handles user registration
# -------------------------------------------------------------------
class SignupForm(forms.ModelForm):
    # Password fields with password input widget
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        # Fields required for creating a new user
        fields = ['username', 'password', 'password2']

    # Custom validation to ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")


# -------------------------------------------------------------------
# LoginForm: handles user login
# -------------------------------------------------------------------
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

