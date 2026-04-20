from django.conf import settings
from django.db import models
from catalog.models import FunkoFigure


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Пользователь'
    )
    figure = models.ForeignKey(
        FunkoFigure,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Фигурка'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
        unique_together = ('user', 'figure')

    def __str__(self):
        return f"{self.user.username} - {self.figure.title} ({self.quantity})"