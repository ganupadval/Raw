

from django.db import models



# Create your models here.
class Form_data(models.Model):

    # event_title= models.CharField(max_length=20)
    name= models.CharField(max_length=30)
    email= models.EmailField(primary_key=True)
    roll_num= models.IntegerField()
    std_id= models.CharField(max_length=15)
    div= models.CharField(max_length=1)
    year= models.CharField(max_length=10)
    phone_num= models.IntegerField()
    is_present= models.BooleanField(default=False)

