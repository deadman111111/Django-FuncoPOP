from django.urls import path
from .views import (
    figure_list,
    figure_detail,
    figure_create,
    figure_update,
    figure_delete,
)

urlpatterns = [
    path('', figure_list, name='figure_list'),
    path('create/', figure_create, name='figure_create'),
    path('<int:pk>/', figure_detail, name='figure_detail'),
    path('<int:pk>/edit/', figure_update, name='figure_update'),
    path('<int:pk>/delete/', figure_delete, name='figure_delete'),
]