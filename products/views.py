from django.shortcuts import render
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