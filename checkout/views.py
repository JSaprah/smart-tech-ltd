from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no products in the bag")
        return redirect(reverse('products'))

    form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': form,
    }

    return render(request, template, context)
