from django.urls import path
from .views import customer_upload_view

urlpatterns = [
    path("customer/upload/", customer_upload_view, name="customer_upload_view"),
]
