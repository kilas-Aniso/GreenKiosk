from django.contrib import admin

# Register your models here.
from .models import Refund
class RefundAdmin(admin.ModelAdmin):
   list_display=( 'item_ordered','requested_time','reason','approval')
admin.site.register(Refund,RefundAdmin)