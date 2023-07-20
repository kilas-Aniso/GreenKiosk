from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
   list_display=( 'order_status','items', 'customer_information' ,'payment_details')
admin.site.register(Order,OrderAdmin)