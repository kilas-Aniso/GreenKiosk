from django.urls import path
from .views import cart_view
from .views import add_to_cart
urlpatterns = [
    path("carts/upload/", add_to_cart, name='add_to_cart'),
    path("carts/cart_view/", cart_view, name='cart_view'),
]