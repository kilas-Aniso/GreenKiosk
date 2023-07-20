from django.contrib import admin

# Register your models here.
from .models import Customer

class customerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "phone_number", "address","email")
    


admin.site.register(Customer,customerAdmin)
    
