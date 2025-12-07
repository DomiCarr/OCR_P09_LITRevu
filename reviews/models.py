# reviews/models.py
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


# -------------------------------------------------------------------
# Ticket model represents a request for a review (like a post)
# -------------------------------------------------------------------
class Ticket(models.Model):
    # Title of the ticket, max 128 characters
    title = models.CharField(max_length=128)

    # Description / details of the ticket, optional, max 2048 characters
    description = models.TextField(max_length=2048, blank=True)

    # User who created the ticket, linked to Django's built-in user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Optional image attached to the ticket
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='ticket_images/'  # store images here
    )

    # Automatically set the creation date/time
    time_created = models.DateTimeField(auto_now_add=True)

    # Human-readable representation of a Ticket instance
    def __str__(self):
        return f"{self.title} ({self.user})"


# -------------------------------------------------------------------
# Review model represents a review made on a Ticket
# -------------------------------------------------------------------
class Review(models.Model):
    # The ticket this review is linked to
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    # Rating of the review, between 0 and 5
    note = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    # Short headline/title for the review
    titre = models.CharField(max_length=128)

    # Detailed review text, optional, max 8192 characters
    commentaire = models.TextField(max_length=8192, blank=True)

    # User who wrote the review
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Automatically set the creation date/time
    time_created = models.DateTimeField(auto_now_add=True)

    # Human-readable representation of a Review instance
    def __str__(self):
        return f"{self.titre} ({self.user})"


# -------------------------------------------------------------------
# UserFollows model represents a "following" relationship between users
# -------------------------------------------------------------------
class UserFollows(models.Model):
    # The follower
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='following',
        on_delete=models.CASCADE
    )

    # The user being followed
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='followed_by',
        on_delete=models.CASCADE
    )

    class Meta:
        # Ensure a user cannot follow the same person more than once
        unique_together = ('user', 'followed_user')

    # Human-readable representation of a UserFollows instance
    def __str__(self):
        return f"{self.user} follows {self.followed_user}"


# -------------------------------------------------------------------
# Publication model represents a book or an article
# -------------------------------------------------------------------
class Publication(models.Model):
    BOOK = "Book"
    ARTICLE = "Article"
    PUB_TYPES = [
        (BOOK, "Book"),
        (ARTICLE, "Article"),
    ]

    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    pub_type = models.CharField(max_length=10, choices=PUB_TYPES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.URLField(
        default="https://dummyimage.com/150x150/cccccc/000000.png&text=No+Image"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.pub_type})"
