from django.urls import path
from .views import customer_list
from .views import customer_create
from .views import customer_detail
from .views import customer_edit



urlpatterns = [
    path('customers/list/', customer_list, name='customer_list'),
    path('customers/create/', customer_create, name='customer_create'),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),
    path('customers/<int:pk>/edit/',customer_edit, name='customer_edit'),
]





