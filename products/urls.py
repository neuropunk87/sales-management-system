from django.urls import path
from products.views import list_products, add_product, edit_product, delete_product

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/add/', add_product, name='add_product'),
    path('products/edit/<int:pk>/', edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', delete_product, name='delete_product')
]
