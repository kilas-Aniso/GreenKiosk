from django.db import models

# Create your models here.
class Notification (models.Model):
    user_name=models.CharField(max_length=32)
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)