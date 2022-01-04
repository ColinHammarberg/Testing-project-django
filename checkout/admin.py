from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'user_account', 'date', 'full_name',
              'email', 'phone_number', 'mobile_number' 'country',
              'postcode', 'town_or_city', 'street_address',
              'county', 'delivery_cost',
              'order_total', 'grand_total', 'charity',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'charity',)

    ordering = ('-date',)
    

admin.site.register(Order, OrderAdmin)