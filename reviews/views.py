from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from .models import Review


# Create your views here.
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(
        request, {'form': form, 'product': product}
        )


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('product_detail', product_id=review.product.id)

    return render(request, 'reviews/confirm_delete.html', {'review': review})
