from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to render the bag contents """

    return render(request, 'bag/bag.html')


def add_product_to_bag(request, product_id):
    """ A view to add products to the bag with the selected quantity """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def update_bag(request, product_id):
    """ A view to update the bag """

    item = get_object_or_404(Product, pk=product_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
        messages.success(request, f'Updated {item.name}')
    else:
        bag.pop(product_id)
        messages.success(request, f'Removed {item.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
