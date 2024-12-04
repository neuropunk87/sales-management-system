from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from sales.models import Sale
from sales.forms import SaleForm


def list_sales(request):
    sales = Sale.objects.select_related('customer', 'seller', 'product').all()
    paginator = Paginator(sales, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sales.html', {'page_obj': page_obj})


def add_sale(request):
    form = SaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_sales')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Add Sale',
        'back_url': reverse('list_sales')
    })


def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    form = SaleForm(request.POST or None, instance=sale)
    if form.is_valid():
        form.save()
        return redirect('list_sales')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Edit Sale',
        'back_url': reverse('list_sales')
    })


def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('list_sales')
    return render(request, 'delete_entity.html', {
        'sale': sale,
        'back_url': reverse('list_sales')
    })
