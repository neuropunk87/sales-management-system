from django.urls import path
from users.views import (list_customers, add_customer, edit_customer, delete_customer,
                         list_sellers, add_seller, edit_seller, delete_seller)

urlpatterns = [
    path('customers/', list_customers, name='list_customers'),
    path('customers/add/', add_customer, name='add_customer'),
    path('customer/edit/<int:pk>/', edit_customer, name='edit_customer'),
    path('customer/delete/<int:pk>/', delete_customer, name='delete_customer'),

    path('sellers/', list_sellers, name='list_sellers'),
    path('sellers/add/', add_seller, name='add_seller'),
    path('sellers/edit/<int:pk>/', edit_seller, name='edit_seller'),
    path('seller/delete/<int:pk>/', delete_seller, name='delete_seller')
]
