# rooter

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth_view import login_view, signup_view, logout_view
from .views.publication_view import list_publications
from reviews.views.ticket_view import create_ticket
from reviews.views.feed_view import feed_view
from reviews.views.review_view import create_review
from reviews.views.review_update import review_update
from reviews.views.review_delete import review_delete
from reviews.views.follow_view import follow_view
from reviews.views.post_view import post_view
from reviews.views.ticket_update import ticket_update
from reviews.views.ticket_delete import ticket_delete


urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('publications/', list_publications, name='publication_list'),

    # Tickets
    path('tickets/new/', create_ticket, name='ticket_create'),
    path('tickets/update/<int:ticket_id>/', ticket_update, name='ticket_update'),
    path('tickets/delete/<int:ticket_id>/', ticket_delete, name='ticket_delete'),

    # Reviews
    path('reviews/new/', create_review, name='review_create'),
    path('reviews/new/<int:ticket_id>/', create_review, name='review_create_ticket'),
    path('reviews/<int:pk>/edit/', review_update, name='review_update'),
    path('reviews/<int:pk>/delete/', review_delete, name='review_delete'),

    # Other
    path('feed/', feed_view, name='feed'),
    path("follow/", follow_view, name="follow"),
    path('posts/', post_view, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
