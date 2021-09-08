from django.shortcuts import render
from .models import Product

# Products

def all_products(request):
    # Should show all products loaded

    products = Products.objects.all()
    
    return render(request, 'products/every_product.html')
