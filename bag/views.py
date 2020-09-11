from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A Views to return the bag page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {}) ## Trying to get session(bag) variable if it already exists and initializing it to an empty dictionary if it doesn't.

    if item_id in list(bag.keys()): ## first check to see if there's a bag variable in the session.
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag ## put the bag variable into the session. Which itself is just a python dictionary.
    return redirect(redirect_url)