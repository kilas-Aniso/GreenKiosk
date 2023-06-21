from django.contrib import admin

# Register your models here.
from .models import Customer

class customerAdmin(admin.ModelAdmin):
    list_display=("firstName", "lastName", "phone_number", "adress","email")
    


admin.site.register(Customer,customerAdmin)
    
