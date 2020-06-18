import django_filters
from django_filters import CharFilter, MultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter
from django import forms
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product Name",
                      widget=forms.TextInput(attrs={'placeholder': 'Enter product name:', 'class': 'form-control mb-2 mr-sm-2'}))
    categories = ModelChoiceFilter(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-2 mr-sm-2'}))

    class Meta:
        model = Product
        fields = ['name', 'categories']
