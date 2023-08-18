from django.urls import path
from .views import process_payment
   
urlpatterns = [
   
    path("payment/orders/<int:order_id>/process_payment/", process_payment, name='process_payment'),
]

    

