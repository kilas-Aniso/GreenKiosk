from django.urls import path;
from .views import feedback_details_views
urlpatterns=[
path("feedback/upload/",feedback_details_views,name="feedback_details_views"),
]