from django.contrib import admin

# Register your models here.
from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
   list_display=('customer_name','delivery_address','delivery_date','order_id','delivery_cost')
admin.site.register(Delivery,DeliveryAdmin)