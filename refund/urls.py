from django.urls import path;
from .views import refund_details_views

urlpatterns=[
path("refund/upload/",refund_details_views,name="refund_details_views"),
]

