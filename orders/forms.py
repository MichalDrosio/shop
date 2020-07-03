from django import forms
from .models import Order
from localflavor.pl.forms import PLPostalCodeField


class OrderCreateForm(forms.ModelForm):
    postal_code = PLPostalCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'adress', 'city', 'phone', 'postal_code']