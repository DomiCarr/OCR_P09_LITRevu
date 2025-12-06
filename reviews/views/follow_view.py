from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from reviews.models import UserFollows
import logging

logger = logging.getLogger(__name__)

@login_required
def follow_view(request):
    user = request.user

    # Ajouter un abonnement
    if request.method == "POST" and "follow_username" in request.POST:
        username_to_follow = request.POST.get("follow_username", "").strip()
        logger.debug("follow_view POST received: %r by user %r", username_to_follow, user.username)
        try:
            target_user = User.objects.get(username=username_to_follow)
            if target_user != user:
                obj, created = UserFollows.objects.get_or_create(
                    user=user, followed_user=target_user
                )
                logger.debug("UserFollows get_or_create returned: created=%s id=%s", created, getattr(obj, "id", None))
        except User.DoesNotExist:
            logger.debug("User to follow not found: %r", username_to_follow)
        return redirect("follow")

    # Listes abonnements et abonnés (noms de champs corrects)
    abonnements = UserFollows.objects.filter(user=user).select_related("followed_user")
    abonnes = UserFollows.objects.filter(followed_user=user).select_related("user")

    context = {
        "abonnements": abonnements,
        "abonnes": abonnes,
    }
    return render(request, "reviews/follow.html", context)
