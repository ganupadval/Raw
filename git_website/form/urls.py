# from django.contrib import admin
from django.urls import path
from form import views


urlpatterns=[
    # path(r'^verify$',views.certificateApi),
    # path(r'^verify/([0-9]+)$',views.certificateApi),
    path('form/',views.formApi),
    path ('formadmin/',views.formAdmin)
    ]

