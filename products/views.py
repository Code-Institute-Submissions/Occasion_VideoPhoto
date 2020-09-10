from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Occasion
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    occasions = None
    sort = None
    direction = None
    if request.GET:
        # Sort function 
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        # Filtering function
        if 'category' in request.GET:
            categories = request.GET['category'].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'occasion' in request.GET:
            occasions = request.GET['occasion'].split(",")
            products = products.filter(occasion__name__in=occasions)
            occasions = Occasion.objects.filter(name__in=occasions)
       # Search function
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(category__friendly_name__icontains=query) | Q(description__icontains=query) | Q(things_include__icontains=query) | Q(package__name__icontains=query) | Q(occasion__friendly_name__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_occasions": occasions,
        "current_sorting": current_sorting,

    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)

