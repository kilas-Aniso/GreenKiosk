from django.urls import path
from .views import place_order, order_view

urlpatterns = [
    path("orders/place_order/", place_order, name='place_order'),
    path("orders/order_view/", order_view, name='order_view'),
]
