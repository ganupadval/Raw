from datetime import date
from functools import partial
from inspect import _void
import json
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Certificate_info, Certificate_info
from .serializers import CertificateSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


#CreateAPIView
class CertificateView(generics.ListAPIView): 
    queryset = Certificate_info.objects.all()
    serializer_class = CertificateSerializer

#handle api requests
@csrf_exempt
def certificateApi (request, format=None):
   
    if request.method =='GET':
        # 
         return render(request, 'form.html')
    elif request.method =='POST':
        
        # THIS SHOULD BE USED TO GET THE CERTIFICATE INFO FROM CERTIFICATE ID
        
        
        data = JSONParser().parse(request)
        
        certificate = Certificate_info.objects.get(crid=data.get('crid'))
        Certificates_serializer =CertificateSerializer(certificate)
        return JsonResponse(Certificates_serializer.data)

@csrf_exempt
def certificateAdminSide (request, format=None):
    
    
    if request.method=='GET':
        # GET ALL CERTIFICATES ISSUED
        Certificate = Certificate_info.objects.all()
        Certificate_serializer = CertificateSerializer(Certificate, many=True)
        return JsonResponse(Certificate_serializer.data, safe=False)
    
    elif request.method=='POST':
    # THIS CAN BE USED ON ADMIN SITE TO ADD CERTIFICATE INFO
        Certificate_data=JSONParser().parse(request)
        Certificate_serializer = CertificateSerializer(data=Certificate_data)
        if Certificate_serializer.is_valid():
            Certificate_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    
    # # SELECTING SPECIFIC CERTIFICATE BY CERTIFICATE BY CRID FOR PATCH & DELETE REQUEST
    #     data= JSONParser().parse(request)
    #     Certificate = Certificate_info.objects.get(crid=data.get('crid')) 

    elif request.method=='PATCH':
        # UPDATE CERTIFICATE INFO
        # SELECTING SPECIFIC CERTIFICATE BY CERTIFICATE BY CRID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        object = Certificate_info.objects.get(crid=data.get('crid')) 
        Certificate_serializer= CertificateSerializer(object, data=data, partial=True)
        if Certificate_serializer.is_valid():
            Certificate_serializer.save();
            return JsonResponse("UPDATED", safe=False)

        return JsonResponse("FAILED", safe=False)

    elif request.method=='DELETE':
        # DELETE CERTIFICATE INFO
         # SELECTING SPECIFIC CERTIFICATE BY CERTIFICATE BY CRID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        Certificate = Certificate_info.objects.get(crid=data.get('crid')) 
        Certificate.delete()
        return JsonResponse("NO_CONTENT", safe=False)
