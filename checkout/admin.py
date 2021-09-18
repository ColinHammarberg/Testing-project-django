from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.

class Personalized_OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'delivery_cost', 
                       'order_total', 'grand_total',)

    fields = ('order_number', 'full_name', 'email', 'country',
              'town_or_city', 'street_address', 'post_address',
              'delivery_cost', 'order_total', 'grand_total')
