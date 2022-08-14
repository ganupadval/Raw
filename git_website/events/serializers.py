from curses import meta
from pyexpat import model
from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields= ('id','title','brief', 'presentor', 'date', 'start_time', 'end_time','venue', 'status', 'learnings', 'pre_req')

