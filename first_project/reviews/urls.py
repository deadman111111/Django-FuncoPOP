from django.urls import path
from .views import review_create, review_update, review_delete, review_list

urlpatterns = [
    path('create/<int:figure_id>/', review_create, name='review_create'),
    path('<int:pk>/edit/', review_update, name='review_update'),
    path('<int:pk>/delete/', review_delete, name='review_delete'),
    path('all/', review_list, name='review_list'),
]