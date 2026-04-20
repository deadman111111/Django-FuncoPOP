from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from catalog.models import FunkoFigure
from .models import CartItem

User = get_user_model()


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('figure')
    total_price = sum(item.figure.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


@login_required
def add_to_cart(request, pk):
    figure = get_object_or_404(FunkoFigure, pk=pk)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        figure=figure,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, 'Фигурка добавлена в корзину.')
    return redirect('cart_detail')


@login_required
def increase_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')


@login_required
def decrease_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.delete()

    messages.success(request, 'Товар удалён из корзины.')
    return redirect('cart_detail')


@admin_required
def admin_cart_list(request):
    users_with_cart = User.objects.filter(cart_items__isnull=False).distinct()
    return render(request, 'cart/admin_cart_list.html', {
        'users_with_cart': users_with_cart
    })


@admin_required
def admin_user_cart(request, user_id):
    user_obj = get_object_or_404(User, pk=user_id)
    cart_items = CartItem.objects.filter(user=user_obj).select_related('figure')
    total_price = sum(item.figure.price * item.quantity for item in cart_items)

    return render(request, 'cart/admin_user_cart.html', {
        'user_obj': user_obj,
        'cart_items': cart_items,
        'total_price': total_price,
    })


@admin_required
def admin_increase_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.quantity += 1
    cart_item.save()

    messages.success(request, 'Количество товара увеличено.')
    return redirect('admin_user_cart', user_id=cart_item.user.pk)


@admin_required
def admin_decrease_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    user_id = cart_item.user.pk

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, 'Количество товара уменьшено.')
    else:
        cart_item.delete()
        messages.success(request, 'Товар удалён из корзины пользователя.')

    return redirect('admin_user_cart', user_id=user_id)


@admin_required
def admin_remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    user_id = cart_item.user.pk
    cart_item.delete()

    messages.success(request, 'Товар удалён из корзины пользователя.')
    return redirect('admin_user_cart', user_id=user_id)