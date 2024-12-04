from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity in Stock")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
