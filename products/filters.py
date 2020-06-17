import django_filters
from django_filters import CharFilter, NumberFilter, MultipleChoiceFilter, ChoiceFilter
from django import forms
from .models import Product


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product Name",
                      widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}))
    # category = MultipleChoiceFilter(choices=Product.category, field_name='category', label="Category",
    #                                 widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Product
        fields = ['name', 'category']
