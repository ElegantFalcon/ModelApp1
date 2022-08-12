from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

from app2.models import CustomerData
from app2.serializers import CSerializer

# Create your views here.
@csrf_exempt
def cust_details(request, id = 0):
    if request.method == 'POST' :
        cust_details = JSONParser().parse(request)
        Customserializer = CSerializer(data = cust_details)
        if Customserializer.is_valid():
            Customserializer.save()
            return JsonResponse({"status" : "success" , "data" : Customserializer.data})
        else :
            return JsonResponse({"status" : "failed" , "data" : Customserializer.errors})

    elif request.method == 'GET' :
        products = CustomerData.objects.all()  

        Customserializer = CSerializer(products, many = True)
        return JsonResponse({"data": Customserializer.data})
    
    elif request.method == 'PUT' :
        products = JSONParser().parse(request)
        productsData = CustomerData.objects.get(id = products['id'])
        cu_sel = CSerializer(productsData, products  )
        if cu_sel.is_valid():
            cu_sel.save()
            return JsonResponse({"status" : "data updated " , "data" : cu_sel.data})
        else :
            return JsonResponse({"status" : "couldnt update data" , "data" : cu_sel.errors})


    elif request.method == 'DELETE' :
        products = JSONParser().parse(request)
        productsData = CustomerData.objects.filter(id = products['id'])
        productsData.delete()
        
        return JsonResponse({"status" : "data deleted " })