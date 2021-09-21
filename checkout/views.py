from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from django.conf import settings
from shoppingbag.context import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 1000)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout_page.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jc76MLMnDjwSmeEPEwE2cabv12LKQgbG2yWYkQ4XsNoanL3uCPm2xp85dEZNRWC836MBExGyYuZLKh6ww1qy3Il00ukscdXr5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)