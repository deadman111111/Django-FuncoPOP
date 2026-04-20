from django import forms
from .models import FunkoFigure


class FunkoFigureForm(forms.ModelForm):
    class Meta:
        model = FunkoFigure
        fields = [
            'title',
            'character_name',
            'franchise',
            'series',
            'price',
            'stock',
            'release_date',
            'description',
            'image',
            'is_available',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'character_name': forms.TextInput(attrs={'class': 'form-input'}),
            'franchise': forms.TextInput(attrs={'class': 'form-input'}),
            'series': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'stock': forms.NumberInput(attrs={'class': 'form-input'}),
            'release_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-input form-textarea', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }