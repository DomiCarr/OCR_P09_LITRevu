from django.urls import path
from .views.auth_view import login_view, signup_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),  # page d'accueil = login
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
