from django.shortcuts import render
from reviews.models import Publication


def list_publications(request):
    publications = Publication.objects.all().order_by("id")
    return render(
        request,
        "reviews/publication_list.html",
        {"publications": publications}
    )
