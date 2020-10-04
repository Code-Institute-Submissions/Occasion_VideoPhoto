from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A Views to return the bag page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # Trying to get session(bag) variable if it already exists and initializing it to an empty dictionary if it doesn't.

    if item_id in list(bag.keys()):  # first check to see if there's a bag variable in the session.
        bag[item_id] += quantity
        messages.success(request, f'Update {product.category.friendly_name} - {product.occasion.friendly_name} quantuty to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.category.friendly_name} - {product.occasion.friendly_name}  to your bag')

    request.session['bag'] = bag  ## put the bag variable into the session. Which itself is just a python dictionary.
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Update {product.category.friendly_name} - {product.occasion.friendly_name} quantuty to {bag[item_id]}')

    else:
        bag.pop(item_id)
        messages.success(request, f'Remove {product.category.friendly_name} - {product.occasion.friendly_name}  from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Remove {product.category.friendly_name} - {product.occasion.friendly_name}  from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
