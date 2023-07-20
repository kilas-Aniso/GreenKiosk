from django.contrib import admin

# Register your models here.
from django.contrib import admin# Register your models here.
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('product','quantity')
admin.site.register(Cart,CartAdmin)