from django.shortcuts import render, get_object_or_404
from .models import Product

# Demonstrating all products available

def all_products(request):
    """ Product display """

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query =

    context = {
        'products': products,
    }

    return render(request, 'products/every_product.html', context)

def product_description(request, product_id):
    """ Product description display """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_description.html', context)

