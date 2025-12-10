# reviews/apps.py
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    # Default type for auto-increment primary keys if not specified in models
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the application; used by Django to register the app, find models,
    # apply migrations, and include in admin
    name = 'reviews'
