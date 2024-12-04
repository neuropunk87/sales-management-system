from django import forms
from django.core.exceptions import ValidationError
from sales.models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity', 'total_amount', 'seller', 'customer']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        product = self.cleaned_data.get('product')
        if product and product.stock_quantity < quantity:
            raise ValidationError(f"Not enough {product.name} in stock.")

        return quantity
