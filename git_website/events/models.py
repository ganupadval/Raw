
from django.db import models

class Event(models.Model):
    title= models.CharField(max_length=20)
    brief= models.CharField(max_length=30)
    presentor= models.CharField(max_length=20)
    date= models.DateField()
    start_time= models.TimeField()
    end_time= models.TimeField()
    venue= models.CharField(max_length=20)
    # status: values
    # 1 - past events 
    # 2 - ongoing events
    # 3 - upcoming events 
    status= models.IntegerField()
    learnings= models.TextField()
    pre_req= models.TextField()