from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from catalog.models import FunkoFigure
from .forms import ReviewForm
from .models import Review


@login_required
def review_create(request, figure_id):
    figure = get_object_or_404(FunkoFigure, pk=figure_id)

    review = Review.objects.filter(user=request.user, figure=figure).first()
    if review:
        messages.error(request, 'Вы уже оставили отзыв на эту фигурку.')
        return redirect('figure_detail', pk=figure.pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.figure = figure
            new_review.save()
            messages.success(request, 'Отзыв успешно добавлен.')
            return redirect('figure_detail', pk=figure.pk)
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'page_name': f'Оставить отзыв на "{figure.title}"',
        'figure': figure,
    })


@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Отзыв успешно обновлён.')
            return redirect('figure_detail', pk=review.figure.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'page_name': 'Редактировать отзыв',
        'figure': review.figure,
    })


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    figure_pk = review.figure.pk

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Отзыв удалён.')
        return redirect('figure_detail', pk=figure_pk)

    return render(request, 'reviews/review_confirm_delete.html', {
        'review': review,
    })


@admin_required
def review_list(request):
    reviews = Review.objects.select_related('user', 'figure').all()
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews
    })