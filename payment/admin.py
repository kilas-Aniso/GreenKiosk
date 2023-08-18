from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_payment = ("amount","method", "payment_status", "payment_date")

admin.site .register(Payment,PaymentAdmin)

