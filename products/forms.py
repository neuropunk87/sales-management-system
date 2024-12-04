from django import forms
from django.core.exceptions import ValidationError
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock_quantity', 'price']

    def clean_stock_quantity(self):
        stock_quantity = self.cleaned_data['stock_quantity']
        if stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative.")
        return stock_quantity

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price
