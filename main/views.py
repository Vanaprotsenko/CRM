from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages

from product.models import Product
from user.models import User
from product.forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/main.html', context={'products': products})


def logout_view(request):
    logout(request)
    return redirect('auth')


def add_product(request):
    if request.user.position in ["Admin", "Manager"]:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Product added successfully.")
                return redirect('product_list')
        else:
            form = ProductForm()
        return render(request, 'main/add_product.html', {'form': form})
    else:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('product_list')


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'main/update_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('product_list')
    return render(request, 'main/delete_product.html', {'product': product})


