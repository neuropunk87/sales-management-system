from django.db import models
from users.models import Customer, Seller
from products.models import Product
from django.core.exceptions import ValidationError


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity Sold")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk:
            old_sale = Sale.objects.get(pk=self.pk)
            difference = self.quantity - old_sale.quantity
        else:
            difference = self.quantity

        if self.product.stock_quantity < difference:
            raise ValidationError(f"Not enough {self.product.name} in stock.")

        self.product.stock_quantity -= difference
        self.product.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.stock_quantity += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Sale of {self.product.name} ({self.quantity}) to {self.customer.first_name}"
