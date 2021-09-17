from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.

def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')


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
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'You have successfully updated your cart by adding another item of the {product.name}. We are happy that you like it.')
        else:
            cart[item_id] = quantity
            messages.success(request, f'You have successfully added the {product.name} to your shopping cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)

def remove_product(request, item_id):
    """Removing product from shopping cart"""
