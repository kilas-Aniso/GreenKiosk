from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback_content = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField()
    ratings = models.CharField(max_length=5)
    Feedback_status = models.CharField(max_length=20)
