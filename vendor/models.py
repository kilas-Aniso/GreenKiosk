from django.db import models

# Create your models here.
class Vendor(models.Model):     
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    store_name=models.CharField(max_length=32)
    contact_number=models.CharField(max_length=10)