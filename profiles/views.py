from django.shortcuts import render

def account(request):
    template = 'profiles/account.html'
    context = {}

    return render(request, template, context)