from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Form_data
from .serializers import FormSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def formApi (request, format=None):
    if request.method=='POST':
        request_data =JSONParser().parse(request)
        serializer =FormSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Invalid Format", safe=False)

def formAdmin(request, format=None):
    if request.method=='GET':
            # GET ALL CERTIFICATES ISSUED
            objects = Form_data.objects.all()
            serializer = FormSerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
        