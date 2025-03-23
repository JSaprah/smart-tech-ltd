from django.shortcuts import render, get_object_or_404, redirect
from .models import Wishlist
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def wishlist(request):

    template = 'wishlist/wishlist.html'

    return render(request, template)
