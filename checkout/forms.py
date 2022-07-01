from django import forms
from .models import Order


class OrderForm(forms.ModelForm)
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'town_or_city',
                  'post_code', 'country', 'county',)