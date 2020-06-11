from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Product

# class Home(ListView):
#     model = Product
#     template_name = '/home-page.html'

def Home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products-section.html', context)


def ProductPage(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'product-page.html', context)
