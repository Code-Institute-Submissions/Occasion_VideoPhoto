from decimal import Decimal
from django.conf import settings

def bag_contects(request):
    bag_items = []
    total = 0.0
    product_count = 0

    grand_total = total * settings.PRECENT_ADVANCE_PAYMENT_OF_FULL_PRICE # 30%
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context