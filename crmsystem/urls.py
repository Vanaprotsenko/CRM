from django.contrib import admin
from django.urls import path

from main.views import product_list

from user.views import auth
from main.download_execl import export_products
from main.views import logout_view, add_product, update_product, delete_product
from main.views import manager_dashboard_view, user_dashboard_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', product_list, name='product_list'),
    path('auth/', auth, name='auth'),
    path('logout/', logout_view, name='logout'),

    path('products/add/', add_product, name='add_product'),
    path('products/<int:product_id>/edit/', update_product, name='update_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),
    path('export/', export_products, name='export_products'),

    path('manager_dashboard/', manager_dashboard_view, name='manager_dashboard'),
    path('user_dashboard/', user_dashboard_view, name='user_dashboard'),
]
