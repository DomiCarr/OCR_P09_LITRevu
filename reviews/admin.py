from django.contrib import admin
from .models import Publication
from .models import Ticket


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_type", "user", "time_created")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created")