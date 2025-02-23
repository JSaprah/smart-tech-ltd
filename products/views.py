from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """ Returns all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
