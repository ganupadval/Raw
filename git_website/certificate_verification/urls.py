# from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from django.conf.urls import urls
# from . import views

# urlpatterns = [
#     urls(r'^verify$', views.certificateApi),
#     urls(r'^/([0-9]+)$)', views.certificateApi)
# ]

from certificate_verification import views


urlpatterns=[
    # path(r'^verify$',views.certificateApi),
    # path(r'^verify/([0-9]+)$',views.certificateApi),
    path('verify/',views.certificateApi),
    path('admin/', views.certificateAdminSide)
    ]

urlpatterns= format_suffix_patterns(urlpatterns)