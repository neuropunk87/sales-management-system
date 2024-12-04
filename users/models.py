from django.db import models


class Seller(models.Model):
    POSITION_CHOICES = [
        ('seller', 'Seller'),
        ('chief_seller', 'Chief Seller'),
        ('head', 'Head of Sales'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_position_display()})"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
