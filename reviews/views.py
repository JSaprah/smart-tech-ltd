from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from .models import Review
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user already has a review for this product
    existing_review = Review.objects.filter(
        product=product, author=request.user).first()
    if existing_review:
        messages.error(
            request, 'You have already submitted a review for this product.')
        return redirect('product_detail', product_id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(
                request, 'Your review has been added successfully!')
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(
        request, 'add_review.html', {'form': form, 'product': product}
    )


@login_required
def delete_review(request, review_id):
    # Retrieve the review
    review = get_object_or_404(Review, id=review_id)

    if review.author != request.user:
        messages.error(
            request, 'You are not authorized to delete this review.')
        return HttpResponseForbidden(
            'You do not have permission to delete this review.')

    if request.method == 'POST':
        product_id = review.product.id
        review.delete()
        messages.success(request, 'Review successfully deleted!')
        return redirect('product_detail', product_id=product_id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
