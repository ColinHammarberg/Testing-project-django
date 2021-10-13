from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

# Shopping cart.


def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')

# Adding a product/item to cart.


def add_product(request, item_id):
    """ User can add items to the cart """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['sizes'].keys():
                cart[item_id]['sizes'][size] += quantity
                messages.success(request, f'You have successfully added the {product.name} to your shopping cart.')
            else:
                cart[item_id]['sizes'][size] = quantity
                messages.success(request, f'You have successfully added the {product.name} to your shopping cart.')
        else:
            cart[item_id] = {'sizes': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'You have successfully updated your cart by adding another item of the {product.name}. We are happy that you like the product.')
        else:
            cart[item_id] = quantity
            messages.success(request, f'You have successfully added the {product.name} to your shopping cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


# Removing product/item from cart.


def remove_product(request, item_id):
    """Remove the selected product/item from the user's/session's cart"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['sizes'][size]
            if not cart[item_id]['sizes']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
