from django.db import models
from cart.models import Cart
from customer.models import Customer
from delivery.models import Delivery
# Create your models here.
class Order(models.Model):
    cart=models.ForeignKey(Cart,null=True,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    delivery=models.ForeignKey(Delivery,null=True,on_delete=models.CASCADE)
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.PositiveIntegerField()