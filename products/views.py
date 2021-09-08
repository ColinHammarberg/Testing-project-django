from django.shortcuts import render
from .models import Product

# Demonstrating all products available

def all_products(request):
    """ Products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/every_product.html', context)
