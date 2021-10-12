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

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append(
                {
                    'item_id': item_id,
                    'quantity': item_data,
                    'charity': item_data,
                    'product': product,
                
                }
            )

        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['sizes'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append(
                    {
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'charity': quantity,
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


