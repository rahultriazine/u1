from django.urls import path
from . import views
from rest_framework import routers
from sales.views import *

urlpatterns = [
    path('add_sales_order/', AddSalesOrder.as_view(), name="add sales"),
    path('addSalesOrderToDistributers/', AddSalesOrder.as_view(), name="addSalesOrderToDostributers"),
    path('add_sales_order_image/', AddSalesOrder.as_view(), name="add sales"),
    path('getlastdate/', getLastdate.as_view(), name="get last records"),
    path('gethistory/', gethistory.as_view(), name="gethistory"),
    path('getsalespdf/', getsalespdf.as_view(), name="getsalespdf"),

]
