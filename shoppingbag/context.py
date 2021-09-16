from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
# Context processor

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

# Required help from previous coding lessons

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += (1 * 2)
        product_count += 1
        cart_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            }
        )

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    
    grand_total = delivery + total

    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context


