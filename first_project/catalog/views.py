from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import FunkoFigure
from .forms import FunkoFigureForm
from accounts.decorators import admin_required
from django.db.models import Sum, Value, IntegerField
from django.db.models.functions import Coalesce

def home(request):
    figures = FunkoFigure.objects.annotate(
        cart_total=Coalesce(
            Sum('cart_items__quantity'),
            Value(0),
            output_field=IntegerField()
        )
    ).filter(cart_total__gt=0).order_by('-cart_total', 'title')[:8]

    return render(request, 'home.html', {'figures': figures})


def figure_list(request):
    figures = FunkoFigure.objects.all()
    return render(request, 'catalog/figure_list.html', {'figures': figures})


def figure_detail(request, pk):
    figure = get_object_or_404(FunkoFigure, pk=pk)
    return render(request, 'catalog/figure_detail.html', {'figure': figure})


@admin_required
def figure_create(request):
    if request.method == 'POST':
        form = FunkoFigureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фигурка успешно добавлена.')
            return redirect('figure_list')
    else:
        form = FunkoFigureForm()

    return render(request, 'catalog/figure_form.html', {
        'form': form,
        'page_name': 'Добавить фигурку'
    })


@admin_required
def figure_update(request, pk):
    figure = get_object_or_404(FunkoFigure, pk=pk)

    if request.method == 'POST':
        form = FunkoFigureForm(request.POST, request.FILES, instance=figure)
        if form.is_valid():
            form.save()
            messages.success(request, 'Фигурка успешно обновлена.')
            return redirect('figure_detail', pk=figure.pk)
    else:
        form = FunkoFigureForm(instance=figure)

    return render(request, 'catalog/figure_form.html', {
        'form': form,
        'page_name': 'Редактировать фигурку'
    })


@admin_required
def figure_delete(request, pk):
    figure = get_object_or_404(FunkoFigure, pk=pk)

    if request.method == 'POST':
        figure.delete()
        messages.success(request, 'Фигурка успешно удалена.')
        return redirect('figure_list')

    return render(request, 'catalog/figure_confirm_delete.html', {'figure': figure})