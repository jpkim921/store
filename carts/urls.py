from django.urls import path

from .views import add_to_cart, remove_from_cart, checkout, order_summary

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart"),
    path('order-summary', order_summary, name="order-summary"),
    path('checkout/', checkout, name="checkout"),
]
