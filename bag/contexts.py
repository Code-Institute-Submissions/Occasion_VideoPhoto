from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contects(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        new_prod_price = product.price * Decimal(settings.PRECENT_ADVANCE_PAYMENT_OF_FULL_PRICE) ## to get 30% av orginal price
        prod_qty = Decimal(quantity * new_prod_price)
        total += quantity * new_prod_price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'prod_qty': prod_qty,
        })

    grand_total = total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context