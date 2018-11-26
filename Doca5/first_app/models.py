from django.db import models
from datetime import datetime,date
from django.utils import timezone
#from doc_app.models import slots

# Create your models here.
class category(models.Model):
    cat_name=models.CharField(max_length=36,unique=True)
    def __str__(self):
        return self.cat_name

class location(models.Model):
    loc_name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.loc_name

class doctor(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,)
    location=models.ForeignKey(location,on_delete=models.CASCADE)
    doc_name=models.CharField(max_length=30,unique=True)
    fees=models.IntegerField()
    rating=models.IntegerField()
    #date=models.DateField()

#class slot(models.Model):
#    slot=models.CharField(max_length=6,default="slot1")

class Appointments(models.Model):
    doc_name=models.CharField(max_length=30,null=True)
    fees=models.IntegerField(null=True)
    rating=models.IntegerField(null=True)
    date=models.DateField(default=datetime.now())
    start_time=models.TimeField(default='12:00')
 #   slot=models.ForeignKey(slot,on_delete=models.CASCADE)