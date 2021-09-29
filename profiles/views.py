from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm

def account(request):
    my_account = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(instance=my_account)
    orders = my_account.orders.all()

    template = 'profiles/account.html'
    context = {       
        'form': form,
        'orders': orders,
        'my_account': my_account,
    }

    return render(request, template, context)