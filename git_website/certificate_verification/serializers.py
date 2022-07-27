from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Certificate_info

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate_info
        fields = ('id', 'name', 'event_name', 'purpose', 'crid', 'date')

