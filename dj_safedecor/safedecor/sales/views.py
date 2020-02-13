from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models import Sale_to_customers,Sale_to_customers_detail
from users.models import Users
from sales.serializers import Sale_to_customersSerializers,Sale_to_customers_detailSerializers
from users.serializers import UsersSerializers
from rest_framework import status
from django.db.models import Q
#from django.core.urlresolvers import resolve



class AddSalesOrder(APIView):
    def post(self,request):
        salesDetails = request.data
        serializer=Sale_to_customersSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
           serializer.save()
           sales_id=serializer.data['id']
           if "data_detail" not in request.data:
               dict = {'massage': 'Image uploaded successfully ', 'status': True, 'data': {'sales_id':sales_id}}
           else:
               sales_id=serializer.data['id']
               if sales_id:
                   for data in request.data['data_detail']:
                       data['sales_id']=sales_id
                       serializer = Sale_to_customers_detailSerializers(data=data)
                       if serializer.is_valid():
                           serializer.save()
                           dict = {'massage': 'Record inserted successfully ', 'status': True, 'data': {'sales_id':data['sales_id']}}
                       else:
                           dict = {'massage': 'Record not updated ', 'status': False, 'data': serializer.errors}
                           return Response(dict, status=status.HTTP_200_OK)
               else:
                   dict = {'massage': 'Record not updated ', 'status': False, 'data': serializer.errors}
        else:
            dict = {'massage': 'Record not updated ', 'status': False, 'data': serializer.errors}
        return Response(dict,status=status.HTTP_200_OK)


class getLastdate(APIView):
    def post(self, request):
        distributer_id = request.data['distributer_id']
        t = request.data['type']
        if t== 'distributer':
            check=Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(type='distributer').first()
            if check:
                lastrecord = Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(type='distributer').last()
                serializer = Sale_to_customersSerializers(lastrecord)
            else:
                dic = {}
                dict = {'massage': 'data not found', 'status': False, 'data': dic}
                return Response(dict, status=status.HTTP_200_OK)
        else:
            #print('else')
            check=Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(~Q(type='distributer')).first()
            if check:
                lastrecord = Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(~Q(type='distributer')).last()
                serializer = Sale_to_customersSerializers(lastrecord)
            else:
                dic = {}
                dict = {'massage': 'data not found', 'status': False, 'data': dic}
                return Response(dict, status=status.HTTP_200_OK)


        dic ={}
        if serializer.data:
            dic['distributer_id'] = serializer.data['distributer_id']
            dic['id'] = serializer.data['id']
            sid = serializer.data['id']
            dic['start_date'] = serializer.data['start_date']
            dic['end_date'] = serializer.data['end_date']
            dic['image'] = serializer.data['image']
            dic['type'] = serializer.data['type']
            lastrecordsdetail = Sale_to_customers_detail.objects.filter(sales_id=sid).values('id','product_id','catalog_code','qty')
            serializer = Sale_to_customers_detailSerializers(lastrecordsdetail,many=True)
            #print(serializer.data)
            dic['detail'] = serializer.data
            if dic:
                dict = {'massage': 'data found', 'status': True, 'data':dic}
            else:
                dict = {'massage': 'data not found', 'status': False, 'data': dic}
        else:
            dict = {'massage': 'data not found', 'status': False, 'data': dic}
        return Response(dict, status=status.HTTP_200_OK)

class gethistory(APIView):
    def post(self, request):
        distributer_id=request.data['distributer_id']
        type=request.data['type']
        month=request.data['month']
        year=request.data['year']
        dic={}
        if type == 'distributer':
            salesdetail = Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(type='distributer').filter(Q(Q(start_date__year=year) & Q(start_date__month=month)) | (Q(end_date__year=year) & Q(end_date__month=month)))
        else:
            salesdetail = Sale_to_customers.objects.filter(distributer_id=distributer_id).filter(~Q(type='distributer')).filter(Q(Q(start_date__year=year) & Q(start_date__month=month)) | ( Q(end_date__year=year) & Q(end_date__month=month)))
        #print(salesdetail.query)
        serializer = Sale_to_customersSerializers(salesdetail,many=True)
        dic = serializer.data
        if dic:
            dict = {'massage': 'data found', 'status': True, 'data': dic}
        else:
            dict = {'massage': 'data not found', 'status': False, 'data': dic}

        return Response(dict, status=status.HTTP_200_OK)

    def get(self, request):
        sid = request.GET["id"]
        #print(sid)
        #lastrecordsdetail = Sale_to_customers_detail.objects.filter(sales_id=sid).values('id', 'product_id','catalog_code', 'qty')

        lastrecordsdetail = Sale_to_customers_detail.objects.filter(sales_id=sid)
        serializer = Sale_to_customers_detailSerializers(lastrecordsdetail, many=True)
        if serializer.data:
            dict = {'massage': 'data found', 'status': True, 'data': serializer.data}
        else:
            dict = {'massage': 'data not found', 'status': False, 'data': serializer.data}
        return Response(dict, status=status.HTTP_200_OK)


class getsalespdf(APIView):
    def get(self,request, *args, **kwargs):
        sid = request.GET["sales_id"]
        salesrecords = Sale_to_customers.objects.filter(id=sid)
        serializer = Sale_to_customersSerializers(salesrecords,many=True)
        dic = {}
        dic1 = serializer.data[0]
        distributer_id = dic1['distributer_id']
        #print(distributer_id)
        users = Users.objects.filter(id=distributer_id)
        serializer = UsersSerializers(users,many=True)
        customer_name = serializer.data[0]['customer_name']

        salesrecordsdetail = Sale_to_customers_detail.objects.filter(sales_id=sid).values('id', 'product_id','catalog_code', 'qty')
        serializer = Sale_to_customers_detailSerializers(salesrecordsdetail, many=True)

        dic2 = serializer.data
        data = {}
        data['sales']=dic1
        data['salesdetail'] = dic2
        data['distributer_name'] = customer_name
        ''' Create pdf and save'''
        filename = 'sales_'+sid+'.pdf'
        template = get_template('sales.html')
        html = template.render(data)
        result = BytesIO()
        file = open("uploadimages/pdf/"+filename, "w+b")
        #current_url = request.path_info
        #print(current_url)
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
        dict = {'massage': 'data found', 'status': True, 'data': 'uploadimages/pdf/'+filename }
        return Response(dict, status=status.HTTP_200_OK)
