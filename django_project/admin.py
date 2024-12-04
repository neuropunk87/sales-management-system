from django.contrib import admin
from users.models import Customer, Seller
from products.models import Product
from sales.models import Sale


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'position', 'hire_date')
    list_editable = ('position',)
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('position', 'hire_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock_quantity', 'price')
    list_editable = ('stock_quantity', 'price')
    search_fields = ('name',)
    list_filter = ('stock_quantity',)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'seller', 'quantity', 'total_amount', 'sale_date')
    search_fields = ('product__name', 'customer__first_name', 'seller__first_name')
    list_filter = ('sale_date',)
    date_hierarchy = 'sale_date'
