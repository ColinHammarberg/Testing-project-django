from django.shortcuts import render, get_object_or_404

from .models import UserAccount

def account(request):
    my_account = get_object_or_404(UserAccount, user=request.user)

    template = 'profiles/account.html'
    context = {
        'my_account': my_account,
    }

    return render(request, template, context)