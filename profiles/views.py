from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from checkout.models import Order
from .models import UserAccount
from django.contrib.auth.decorators import login_required
from .forms import UserAccountForm


def account(request):
    my_account = get_object_or_404(UserAccount, user=request.user)
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=my_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account details updated!')

    form = UserAccountForm(instance=my_account)
    orders = my_account.orders.all()

    template = 'profiles/account.html'
    context = {       
        'form': form,
        'orders': orders,
        'my_account': my_account,
    }

    return render(request, template, context)


def previous_orders(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/order_success.html'
    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, template, context)



def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, 'Account deleted!')

    return redirect('home')



