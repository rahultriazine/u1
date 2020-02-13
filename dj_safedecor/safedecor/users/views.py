from django.shortcuts import render
from users.models import Users,Distributer_Catalog,Product_Catalog
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UsersSerializers,Product_CatalogSerializers,Distributer_CatalogSerializers
from rest_framework import status
from django.db.models import Q
# Create your views here.
class DistributersList(APIView):
    def get(self, request):
        # import ipdb;ipdb.set_trace()
        userdetail = Users.objects.all().exclude(Q(role = 1)|Q(id=request.GET['ingore_id']))
        serializer = UsersSerializers(userdetail, many=True)
        if serializer.data:
           dict = {'massage': 'data found', 'status': True,'data':serializer.data}
        else:
           dict = {'massage': 'data not found', 'status': False,'data':serializer.data}
        return Response(dict,status=status.HTTP_200_OK)

class UserLogin(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        userdetail=Users.objects.filter(email=email,password=password)
        serializer = UsersSerializers(userdetail, many=True)
        dicts=[]
        if serializer.data:
            distributer_id=serializer.data[0]['id']
            distributor_detail=Distributer_Catalog.objects.filter(distributer_id=distributer_id)
            #print(userdetail)
            distributer_details = Distributer_CatalogSerializers(distributor_detail, many=True)           
            #print(distributer_details.data)
            serializer.data[0]['distributer_catalog']=[]
            dicts.append(serializer.data[0])
            for distributer_detailss in distributer_details.data:
                distrubuterData={}
                distrubuterData['distributer_id'] =distributer_detailss['distributer_id']  
                distrubuterData['catalog_code'] =distributer_detailss['catalog_code']  
                distrubuterData['catalog_name'] =distributer_detailss['catalog_name'] 
                distrubuterData['catalog_image'] =distributer_detailss['catalog_image']             
                serializer.data[0]['distributer_catalog'].append(distrubuterData)

            dict = {'massage': 'login successfull', 'status': True, 'data':dicts[0]}
        else:
            dict = {'massage': 'Invalid login details', 'status': False,'data':dicts}
        # responseList = [dict]
        return Response(dict, status=status.HTTP_200_OK)

class DistributersProducts(APIView):
     def post(self, request):
        distributer_id=request.data['distributer_id']
        # import ipdb;ipdb.set_trace()
        catalog_codes = Distributer_Catalog.objects.filter(distributer_id=distributer_id).values_list('catalog_code', flat=True)
        products = Product_Catalog.objects.filter(catalog_code__in=catalog_codes).all()
        serializer = Product_CatalogSerializers(products, many=True)
        print(serializer.data)
        if serializer.data:
           dict = {'massage': 'data found', 'status': True,'data':serializer.data}
        else:
           dict = {'massage': 'data not found', 'status': False,'data':serializer.data}
        return Response(dict,status=status.HTTP_200_OK)

class GetCatalog(APIView):
    def post(self, request):
        # import ipdb;ipdb.set_trace()
        distributer_id = request.data['distributer_id']
        distributerCatalog = Distributer_Catalog.objects.filter(distributer_id=distributer_id)
        serializer = Distributer_CatalogSerializers(distributerCatalog, many=True)
        if serializer.data:
           dict = {'massage': 'data found', 'status': True,'data':serializer.data}
        else:
           dict = {'massage': 'data not found', 'status': False,'data':serializer.data}
        return Response(dict,status=status.HTTP_200_OK)