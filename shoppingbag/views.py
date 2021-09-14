from django.shortcuts import render, redirect

# Create your views here.

def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')


def add_product(request, item_id):
    """ User can add items to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

    

