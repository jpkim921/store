from django.urls import path

from .views import Home, ProductPage

app_name = 'mainapp'

urlpatterns = [
    # path('', Home.as_view(), name="home"),
    path('', Home, name="home"),
    path('products/<slug:slug>/', ProductPage, name="productpage")
]
