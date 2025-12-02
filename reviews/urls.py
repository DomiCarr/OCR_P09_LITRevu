# reviews/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth_view import login_view, signup_view, logout_view
from .views.publication_view import list_publications
from reviews.views.ticket_view import create_ticket, update_ticket
from reviews.views.feed_view import feed_view

urlpatterns = [
    path('', login_view, name='login'),  # page d'accueil = login
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('publications/', list_publications, name='publication_list'),
    path('tickets/new/', create_ticket, name='create_ticket'),
    path('tickets/update/<int:ticket_id>/', update_ticket, name='update_ticket'),
    path('feed/', feed_view, name='feed'),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
