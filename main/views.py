import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product
from product.forms import ProductForm

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def product_list(request):
    products = Product.objects.all()
    logging.info('Product list viewed.')
    return render(request, 'main/main.html', context={'products': products})


def logout_view(request):
    request.session.flush()
    logging.info(f'User {request.session.get("user_id")} logged out.')
    return redirect('auth')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            logging.info(f'Product added: {form.instance.title}.')
            messages.success(request, "Product added successfully.")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            logging.info(f'Product updated: {product.title}.')
            messages.success(request, "Product updated successfully.")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'main/update_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        logging.info(f'Product deleted: {product.title}.')
        messages.success(request, "Product deleted successfully.")
        return redirect('product_list')
    return render(request, 'main/delete_product.html', {'product': product})


def admin_dashboard_view(request):
    if request.session.get('user_id') and request.session.get('role') == "admin":
        logging.info('Admin dashboard accessed.')
        return render(request, 'main/main.html')
    return redirect('product_list')


def manager_dashboard_view(request):
    if request.session.get('user_id') and request.session.get('role') == "manager":
        products = Product.objects.all()
        logging.info('Manager dashboard accessed.')
        return render(request, 'user/manager.html', context={'products': products})
    return redirect('manager_dashboard')


def user_dashboard_view(request):
    if request.session.get('user_id') and request.session.get('role') == "user":
        products = Product.objects.all()
        logging.info('User dashboard accessed.')
        return render(request, 'user/user.html', context={'products': products})
    return redirect('user_dashboard')
