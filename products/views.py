from django.shortcuts import render, get_object_or_404
from .models import Product
from .filters import ProductFilter

def Home(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {
        'products': products,
        'myFilter': myFilter
    }
    return render(request, 'products/products-section.html', context)


def ProductPage(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'product-page.html', context)
