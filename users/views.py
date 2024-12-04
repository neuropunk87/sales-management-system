from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from users.models import Customer, Seller
from users.forms import CustomerForm, SellerForm


def list_customers(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customers.html', {'page_obj': page_obj})


def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_customers')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Add Customer',
        'back_url': reverse('list_customers')
    })


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('list_customers')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Edit Customer',
        'back_url': reverse('list_customers')
    })


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('list_customers')
    return render(request, 'delete_entity.html', {
        'customer': customer,
        'back_url': reverse('list_customers')
    })


def list_sellers(request):
    sellers = Seller.objects.all()
    paginator = Paginator(sellers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sellers.html', {'page_obj': page_obj})


def add_seller(request):
    form = SellerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_sellers')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Add Seller',
        'back_url': reverse('list_sellers')
    })


def edit_seller(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    form = SellerForm(request.POST or None, instance=seller)
    if form.is_valid():
        form.save()
        return redirect('list_sellers')
    return render(request, 'add_or_edit_entity.html', {
        'form': form,
        'title': 'Edit Seller',
        'back_url': reverse('list_sellers')
    })


def delete_seller(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == 'POST':
        seller.delete()
        return redirect('list_sellers')
    return render(request, 'delete_entity.html', {
        'seller': seller,
        'back_url': reverse('list_sellers')
    })
