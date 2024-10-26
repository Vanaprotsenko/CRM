from django.contrib import admin
from django.urls import path

from main.views import product_list

from user.views import auth, users_list, edit_user
from main.views import logout_view, add_product, update_product, delete_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', product_list, name='product_list'),
    path('auth/', auth, name='auth'),
    path('users/', users_list, name='users_list'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('logout/', logout_view, name='logout'),
    path('products/<int:user_id>/add/', add_product, name='add_product'),
    path('products/<int:product_id>/edit/', update_product, name='update_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),
]
