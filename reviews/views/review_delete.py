# reviews/views/reviews_delete.py
from django.shortcuts import get_object_or_404, redirect
from reviews.models import Review
from django.contrib.auth.decorators import login_required


@login_required
def review_delete(request, pk):
    """Delete a review created by the logged-in user."""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    review.delete()
    return redirect('post')  # matches the posts list view
