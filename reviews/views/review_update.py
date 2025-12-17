# reviews/views/reviews_update.py
from django.shortcuts import get_object_or_404, redirect, render
from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required


@login_required
def review_update(request, pk):
    """Edit a review created by the logged-in user."""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('post')  # matches the posts list view
    else:
        form = ReviewForm(instance=review)
    return render(
        request,
        'reviews/review_create.html',
        {
            'review_form': form,
            'ticket': review.ticket}
        )
