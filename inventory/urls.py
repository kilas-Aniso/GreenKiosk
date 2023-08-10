from django.urls import path 
from .views import product_list, product_upload_view
from .views import product_detail
from .views import product_update_view  


urlpatterns= [
    path("products/upload/", product_upload_view ,
         name="product_upload_views"),

    path("products/list",product_list,  name="product_list_view"),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("product/edit/<int:id>/",product_update_view, name="product_update_view")

         ]



