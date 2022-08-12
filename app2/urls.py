from django.urls import path
from app2 import views


urlpatterns = [
    path('cu_det' , views.cust_details , name = 'customer_details' )
]