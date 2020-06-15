from django.urls import path

from .views import add_to_cart, remove_from_cart, checkout

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart"),
    path('checkout/', checkout, name="checkout"),
]
