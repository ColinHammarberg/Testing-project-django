from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

# Checkout view.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Add some products to your cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout_page.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
    


