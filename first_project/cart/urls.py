from django.urls import path
from .views import (
    cart_detail,
    add_to_cart,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    admin_cart_list,
    admin_user_cart,
    admin_increase_quantity,
    admin_decrease_quantity,
    admin_remove_from_cart,
)

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('increase/<int:pk>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:pk>/', decrease_quantity, name='decrease_quantity'),
    path('remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),

    path('admin-carts/', admin_cart_list, name='admin_cart_list'),
    path('admin-carts/<int:user_id>/', admin_user_cart, name='admin_user_cart'),
    path('admin-carts/item/<int:pk>/increase/', admin_increase_quantity, name='admin_increase_quantity'),
    path('admin-carts/item/<int:pk>/decrease/', admin_decrease_quantity, name='admin_decrease_quantity'),
    path('admin-carts/item/<int:pk>/remove/', admin_remove_from_cart, name='admin_remove_from_cart'),
]