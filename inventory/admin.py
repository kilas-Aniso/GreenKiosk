from django.contrib import admin

# import your products
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("name", "price","quantity","date_created")


admin.site.register(Product,ProductAdmin)