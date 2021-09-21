from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout_page.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jc76MLMnDjwSmeEPEwE2cabv12LKQgbG2yWYkQ4XsNoanL3uCPm2xp85dEZNRWC836MBExGyYuZLKh6ww1qy3Il00ukscdXr5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)