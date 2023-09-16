from django.urls import path
from .views import CustomerListView, CustomerDetailView

urlpatterns = [
    path('customers/list/', CustomerListView.as_view(), name='customer_list_view'),
    path('customers/<int:id>/', CustomerDetailView.as_view(), name='customer_Detail_view'),
]
