from django.shortcuts import render

# Views - Home page


def index(request):
    return render(request, 'home/index.html')
