from django import forms
from users.models import Customer, Seller


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'phone', 'email', 'position', 'hire_date']
