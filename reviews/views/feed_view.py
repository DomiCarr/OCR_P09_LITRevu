from django.shortcuts import render

def feed_view(request):
    # TODO: implémenter la logique du flux
    return render(request, "reviews/feed.html")
