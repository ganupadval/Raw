from http.client import HTTPResponse
from django.shortcuts import render
from .serializers import EventSerializer
from .models import Event
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def eventPage(request, format=None):
     if request.method=='GET':
        # GET ALL Ongoing Events 
        event = Event.objects.filter(status=2)
        Event_serializer = EventSerializer(event, many=True)
        return JsonResponse(Event_serializer.data, safe=False)
    

@csrf_exempt
def eventAdminSide (request, format=None):
      
    if request.method=='POST':
    # THIS CAN BE USED ON ADMIN SITE TO ADD Event INFO
        Event_data=JSONParser().parse(request)
        Event_serializer = EventSerializer(data=Event_data)
        if Event_serializer.is_valid():
            Event_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    
    # SELECTING SPECIFIC Event BY Event BY ID FOR PATCH & DELETE REQUEST
    #     data= JSONParser().parse(request)
    #     event = Event.objects.get(id=data.get('id')) 

    elif request.method=='PATCH':
        # UPDATE Event INFO
        # SELECTING SPECIFIC Event BY Event BY ID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        object = Event.objects.get(id=data.get('id')) 
        Event_serializer= EventSerializer(object, data=data, partial=True)
        if Event_serializer.is_valid():
            Event_serializer.save();
            return JsonResponse("UPDATED", safe=False)

        return JsonResponse("FAILED", safe=False)

    elif request.method=='DELETE':
        # DELETE Event INFO
         # SELECTING SPECIFIC Event BY Event BY ID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        event = Event.objects.get(id=data.get('id')) 
        event.delete()
        return JsonResponse("DELETED", safe=False)