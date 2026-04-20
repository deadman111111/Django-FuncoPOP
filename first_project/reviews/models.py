from django.conf import settings
from django.db import models
from catalog.models import FunkoFigure


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Пользователь'
    )
    figure = models.ForeignKey(
        FunkoFigure,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Фигурка'
    )
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    is_approved = models.BooleanField(default=True, verbose_name='Одобрено')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
        unique_together = ('user', 'figure')

    def __str__(self):
        return f"Отзыв {self.user.username} на {self.figure.title}"