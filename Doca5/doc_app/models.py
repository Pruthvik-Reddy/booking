from django.db import models
from first_app.models import doctor
from datetime import datetime,date

class slots(models.Model):
    doc_name=models.ForeignKey(doctor,on_delete=models.CASCADE)
    #doc_name=models.CharField(max_length=50,unique=True)
    date=models.DateField()
    start_time=models.TimeField()
    number=models.CharField(max_length=100)