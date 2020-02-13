from django.urls import path
from . import views
from rest_framework import routers
from users.views import *

#app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('distributerslist/', DistributersList.as_view(), name="distributerslist"),
    path('productslist/', DistributersProducts.as_view(), name="DistributersProducts"),
    path('getcatalog/', GetCatalog.as_view(), name="get catalog"),
   # path('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
]
