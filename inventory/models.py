from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8 ,decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now=True)
    quantity=models.PositiveIntegerField()
    ProductCategory = models.CharField

    # next step is we need this model discoverable by the project
    # to do that we go to settings.py
    # 




