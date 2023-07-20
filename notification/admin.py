from django.contrib import admin

# Register your models here.
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display=("user_name","content","date_created")
admin.site.register(Notification,NotificationAdmin)