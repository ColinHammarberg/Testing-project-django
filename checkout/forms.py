from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Form:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'town_or_city',
                  'postcode', 'country',
                  'county', ['charity_choices'])


    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County',
            ['charity_choices']: 'Charity',
        }
         

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = True

        
        