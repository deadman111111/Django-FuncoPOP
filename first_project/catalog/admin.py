from django.contrib import admin
from .models import FunkoFigure


@admin.register(FunkoFigure)
class FunkoFigureAdmin(admin.ModelAdmin):
    list_display = ('title', 'character_name', 'franchise', 'price', 'stock', 'is_available')
    list_filter = ('franchise', 'is_available')
    search_fields = ('title', 'character_name', 'franchise')