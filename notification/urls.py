from django.urls import path;
from .views import notification_details_views
urlpatterns=[
path("notification/upload/",notification_details_views,name="notification_details_views"),
]