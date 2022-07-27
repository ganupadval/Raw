from datetime import date
from django.db import models

# Create your models here.
class Certificate_info(models.Model):
    name = models.CharField(max_length=20,)
    event_name = models.CharField(max_length=50,)
    purpose = models.CharField(max_length=15,)
    crid = models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_created=True)