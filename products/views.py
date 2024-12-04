from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from products.models import Product
from products.forms import ProductForm


def list_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Add Product',
        'back_url': reverse('list_products')
    })


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Edit Product',
        'back_url': reverse('list_products')
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'delete_entity.html', {
        'product': product,
        'back_url': reverse('list_products')
    })
