from django.urls import path
from reports.views import generate_report

urlpatterns = [
    path('reports/customers-by-seller/', generate_report, {'report_type': 'customers_by_seller'},
         name='customers_by_seller'),
    path('reports/sales-by-date/', generate_report, {'report_type': 'sales_by_date'},
         name='sales_by_date'),
    path('reports/sellers-by-product/', generate_report, {'report_type': 'sellers_by_product'},
         name='sellers_by_product'),
    path('reports/customers-by-product/', generate_report, {'report_type': 'customers_by_product'},
         name='customers_by_product'),
    path('reports/total-sales-by-date/', generate_report, {'report_type': 'total_sales_by_date'},
         name='total_sales_by_date'),
    path('reports/top-product/', generate_report, {'report_type': 'top_selling_product'},
         name='top_selling_product'),
    path('reports/top-seller/', generate_report, {'report_type': 'top_seller'}, name='top_seller'),
    path('reports/top-customer/', generate_report, {'report_type': 'top_customer'}, name='top_customer'),
    path('reports/top-product-by-period/', generate_report, {'report_type': 'top_product_by_period'},
         name='top_product_by_period'),
    path('reports/top_seller_by_period/', generate_report, {'report_type': 'top_seller_by_period'},
         name='top_seller_by_period'),
    path('reports/top_customer_by_period/', generate_report, {'report_type': 'top_customer_by_period'},
         name='top_customer_by_period'),
]
