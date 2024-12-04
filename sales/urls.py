from django.urls import path
from sales.views import list_sales, add_sale, edit_sale, delete_sale

urlpatterns = [
    path('sales/', list_sales, name='list_sales'),
    path('sales/add/', add_sale, name='add_sale'),
    path('sales/edit/<int:pk>/', edit_sale, name='edit_sale'),
    path('sales/delete/<int:pk>/', delete_sale, name='delete_sale')
]
