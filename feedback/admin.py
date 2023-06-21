from django.contrib import admin

# Register your models here.
from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_feedback = ("feedback_content","user_image","date","ratings","feedback_status")

admin.site.register(Feedback,FeedbackAdmin)