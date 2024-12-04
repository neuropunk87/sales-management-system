from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from users.models import Seller, Customer
from products.models import Product
from sales.models import Sale
from datetime import datetime


def generate_report(request, report_type):
    sellers = Seller.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()

    results = None
    no_results = False
    selected_seller = None
    selected_product = None
    selected_date = None
    selected_start_date = None
    selected_end_date = None

    is_period_based = report_type in ['top_product_by_period', 'top_seller_by_period', 'top_customer_by_period']
    show_generate_button = report_type not in ['top_selling_product', 'top_seller', 'top_customer']

    if report_type == 'customers_by_seller':
        seller_id = request.GET.get('seller_id')
        if seller_id:
            selected_seller = get_object_or_404(Seller, id=seller_id)
            results = Customer.objects.filter(sale__seller=selected_seller).distinct()
            if not results:
                no_results = True

    elif report_type == 'sales_by_date':
        sale_date = request.GET.get('sale_date')
        if sale_date:
            try:
                selected_date = datetime.strptime(sale_date, "%Y-%m-%d").date()
                results = Sale.objects.filter(sale_date__date=selected_date)
                if not results.exists():
                    no_results = True
            except ValueError:
                results = "Invalid date format. Please use YYYY-MM-DD."

    elif report_type == 'sellers_by_product':
        product_id = request.GET.get('product_id')
        if product_id:
            selected_product = get_object_or_404(Product, id=product_id)
            results = Seller.objects.filter(sale__product=selected_product).distinct()
            if not results:
                no_results = True

    elif report_type == 'customers_by_product':
        product_id = request.GET.get('product_id')
        if product_id:
            selected_product = get_object_or_404(Product, id=product_id)
            results = Customer.objects.filter(sale__product=selected_product).distinct()
            if not results:
                no_results = True

    elif report_type == 'total_sales_by_date':
        sale_date = request.GET.get('sale_date')
        if sale_date:
            try:
                selected_date = datetime.strptime(sale_date, "%Y-%m-%d").date()
                total_sales = (
                        Sale.objects.filter(sale_date__date=selected_date)
                        .aggregate(Sum('total_amount'))['total_amount__sum'] or 0
                )
                results = f"Total Sales: ${total_sales}"
                if total_sales == 0:
                    no_results = True
            except ValueError:
                results = "Invalid date format. Please use YYYY-MM-DD."

    elif report_type == 'top_selling_product':
        products = (
            Product.objects.annotate(total_quantity=Sum('sale__quantity'))
            .filter(total_quantity__isnull=False)
        )
        top_product = products.order_by('-total_quantity').first()
        results = [top_product] if top_product else []
        if not results:
            no_results = True

    elif report_type == 'top_seller':
        sellers = (
            Seller.objects.annotate(total_sales=Sum('sale__total_amount'))
            .filter(total_sales__isnull=False)
        )
        top_seller = sellers.order_by('-total_sales').first()
        results = [top_seller] if top_seller else []
        if not results:
            no_results = True

    elif report_type == 'top_customer':
        customers = (
            Customer.objects.annotate(total_purchases=Sum('sale__total_amount'))
            .filter(total_purchases__isnull=False)
        )
        top_customer = customers.order_by('-total_purchases').first()
        results = [top_customer] if top_customer else []
        if not results:
            no_results = True

    elif report_type == 'top_product_by_period':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        try:
            selected_start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
            selected_end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None

            if selected_start_date and selected_end_date:
                top_product_by_date = (
                    Product.objects.filter(
                        sale__sale_date__range=(selected_start_date, selected_end_date)
                    )
                    .annotate(total_sold=Sum('sale__quantity'))
                    .order_by('-total_sold')
                    .first()
                )
                results = [top_product_by_date] if top_product_by_date else []
                if not results:
                    no_results = True
        except ValueError:
            results = "Invalid date format. Please use YYYY-MM-DD."

    elif report_type == 'top_seller_by_period':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        try:
            selected_start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
            selected_end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None

            if selected_start_date and selected_end_date:
                top_seller_by_date = (
                    Seller.objects.filter(
                        sale__sale_date__range=(selected_start_date, selected_end_date)
                    )
                    .annotate(total_sales=Sum('sale__total_amount'))
                    .order_by('-total_sales')
                    .first()
                )
                results = [top_seller_by_date] if top_seller_by_date else []
                if not results:
                    no_results = True
        except ValueError:
            results = "Invalid date format. Please use YYYY-MM-DD."

    elif report_type == 'top_customer_by_period':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        try:
            selected_start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
            selected_end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None

            if selected_start_date and selected_end_date:
                top_customer_by_date = (
                    Customer.objects.filter(
                        sale__sale_date__range=(selected_start_date, selected_end_date)
                    )
                    .annotate(total_purchases=Sum('sale__total_amount'))
                    .order_by('-total_purchases')
                    .first()
                )
                results = [top_customer_by_date] if top_customer_by_date else []
                if not results:
                    no_results = True
        except ValueError:
            results = "Invalid date format. Please use YYYY-MM-DD."

    return render(request, 'report.html', {
        'report_type': report_type,
        'sellers': sellers,
        'products': products,
        'customers': customers,
        'results': results,
        'no_results': no_results,
        'selected_seller': selected_seller,
        'selected_product': selected_product,
        'selected_date': selected_date,
        'selected_start_date': selected_start_date,
        'selected_end_date': selected_end_date,
        'is_period_based': is_period_based,
        'show_generate_button': show_generate_button,
    })
