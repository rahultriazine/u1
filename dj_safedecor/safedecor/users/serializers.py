from rest_framework import serializers
from . models import Users,Product_Catalog,Distributer_Catalog


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Users
        fields = ('id','customer_name', 'role','email')
        #fields = '__all__'

class Product_CatalogSerializers(serializers.ModelSerializer):
     class Meta:
         model = Product_Catalog
         fields = '__all__'

class Distributer_CatalogSerializers(serializers.ModelSerializer):
     class Meta:
         model =  Distributer_Catalog
         # fields = ('firstname','lastname')
         fields = '__all__'