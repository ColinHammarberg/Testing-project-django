from django.shortcuts import render

# Create your views here.

def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')
