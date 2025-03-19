from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no products in the bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QyDxQ2N6Rlkdg5uFstd1SMHJJBgw5bMHgdHlJ5jEIkbgpHaCpHuWVjFqSsabCWs4W0iwKe8OQbtmKotLU1nHd9S00O5JVVZAk',
        'client_secret': 'sk_test_51QyDxQ2N6Rlkdg5uXDBFWQZSDO07jOc20fWgmVY76BvGZClKukArVIQMZAkClVJ1tPnbgqCNWfwS54YN9F5cbUuI00eLinfh0r',
    }

    return render(request, template, context)
