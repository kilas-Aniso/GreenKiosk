from django.contrib import admin

from.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","date_created", "image")
    


admin.site.register(Product,ProductAdmin)


# Register your models here.

