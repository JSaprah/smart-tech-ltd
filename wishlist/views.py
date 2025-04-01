from django.shortcuts import render, get_object_or_404, redirect
from .models import Wishlist, WishlistItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def wishlist(request):
    """ A view to display the wishlist """
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    except Wishlist.DoesNotExist:
        wishlist_items = []

    context = {'wishlist_items': wishlist_items}
    template = 'wishlist/wishlist.html'

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist """
    product = get_object_or_404(Product, id=product_id)

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    wishlist_item, item_created = WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )

    if item_created:
        messages.success(request, "Added to your wishlist.")
    else:
        messages.info(request, "This product is already in your wishlist.")

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove products from the wishlist """

    # Get the user's wishlist
    wishlist = Wishlist.objects.get(user=request.user)

    # Attempt to delete the item
    deleted_count, _ = WishlistItem.objects.filter(wishlist=wishlist, product_id=product_id).delete()

    if deleted_count > 0:
        messages.info(request, "Removed from your wishlist.")
    else:
        messages.warning(request, "Item could not be removed.")

    return redirect(request.META.get('HTTP_REFERER', '/'))
