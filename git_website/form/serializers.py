from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Form_data

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form_data
        fields = ( 'name', 'email', 'roll_num', 'std_id', 'div','year', 'phone_num','is_present' )

