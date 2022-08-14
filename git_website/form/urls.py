# from django.contrib import admin
from django.urls import path
from form import views


urlpatterns=[
    
    path('form/',views.formApi),
    path ('form-admin/',views.formAdmin)
    ]

