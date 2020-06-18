import django_filters
from django_filters import CharFilter, MultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter
from django import forms
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product Name",
                      widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}))
    categories = ModelChoiceFilter(queryset=Category.objects.all(), widget=forms.Select)
                                    

    class Meta:
        model = Product
        fields = ['name', 'categories']
