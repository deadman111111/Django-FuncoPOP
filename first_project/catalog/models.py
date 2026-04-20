from django.db import models


class FunkoFigure(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    character_name = models.CharField(max_length=255, verbose_name='Персонаж')
    franchise = models.CharField(max_length=255, verbose_name='Франшиза')
    series = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Серия'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    stock = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    release_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата выпуска'
    )
    image = models.ImageField(
        upload_to='figures/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    is_available = models.BooleanField(default=True, verbose_name='Доступна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Фигурка'
        verbose_name_plural = 'Фигурки'
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.franchise}"