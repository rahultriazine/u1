from rest_framework import serializers
from .models import Sale_to_customers,Sale_to_customers_detail


class Sale_to_customersSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Sale_to_customers
        #fields = ('id','customer_name', 'role','email')
        fields = '__all__'


class Sale_to_customers_detailSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Sale_to_customers_detail
        fields = '__all__'

