import django_filters
from django_filters import CharFilter, MultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter
from django import forms
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product Name",
                      widget=forms.TextInput(attrs={'placeholder': 'Enter product name:', 'class': 'form-control form-control-sm'}))
    categories = ModelChoiceFilter(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Product
        fields = ['name', 'categories']
