from django.shortcuts import render, redirect

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
    print(request.session['bag'])
    
    return redirect(redirect_url)