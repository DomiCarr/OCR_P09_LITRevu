# reviews/views/auth_view.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from reviews.forms.auth_forms import SignupForm, LoginForm


# -------------------------------------------------------------------
# Signup view
# -------------------------------------------------------------------
def signup_view(request):
    """
    Handles user registration.
    - GET: displays signup form
    - POST: validates and creates user, redirects to login
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create new user
            form.save()
            messages.success(request, "User created, please log in")
            return redirect('login')
        else:
            # Form invalid: display errors
            messages.error(request, "Please correct the errors below")
    else:
        form = SignupForm()

    # Render signup page with form
    return render(request, 'reviews/signup.html', {'form': form})


# -------------------------------------------------------------------
# Login view
# -------------------------------------------------------------------
def login_view(request):
    """
    Handles user login.
    - GET: displays login form
    - POST: authenticates user and redirects to feed
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('feed')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = LoginForm()

    # Render login page with form
    return render(request, 'reviews/login.html', {'form': form})


# -------------------------------------------------------------------
# Logout view
# -------------------------------------------------------------------
def logout_view(request):
    """
    Logs out the current user and redirects to login page.
    """
    logout(request)
    return redirect('login')
