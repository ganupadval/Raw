from django.urls import path
from . import views

urlpatterns=[
    
    path('event/admin/', views.eventAdminSide),
    path('event/', views.eventPage)
    ]

