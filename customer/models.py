from django.db import models
from django.contrib.auth.models import User# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=32)