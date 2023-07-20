from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
   list_display=("first_name","last_name","store_name","contact_number")
admin.site.register(Vendor,VendorAdmin)