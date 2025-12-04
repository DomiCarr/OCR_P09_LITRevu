from django.contrib import admin
from .models import Publication, Ticket, Review, UserFollows

# -------------------------------------------------------------------
# Publication admin
# -------------------------------------------------------------------
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_type", "user", "time_created")

# -------------------------------------------------------------------
# Ticket admin
# -------------------------------------------------------------------
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created")

# -------------------------------------------------------------------
# Review admin
# -------------------------------------------------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "ticket", "user", "rating", "time_created")
    list_filter = ("rating", "time_created")
    search_fields = ("headline", "body", "user__username", "ticket__title")

# -------------------------------------------------------------------
# UserFollows admin
# -------------------------------------------------------------------
@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user")
    search_fields = ("user__username", "followed_user__username")
