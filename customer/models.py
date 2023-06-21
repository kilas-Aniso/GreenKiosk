from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName=models.CharField(max_length=32)
    lastName=models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    email = models.EmailField()
    adress=models.CharField(max_length=32)

