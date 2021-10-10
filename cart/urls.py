from django.urls import path

from cart.views import add_to_cart, delete_from_cart, order_details

urlpatterns = [
    path('add/',add_to_cart, name="add_cart"),
    path('remove/', delete_from_cart, name="remove_cart"),
    path('order/', order_details, name="order_cart"),
]
