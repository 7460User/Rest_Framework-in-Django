from django.db import models
# Create your models here.
class Wipro_Model(models.Model):
    empname=models.CharField(max_length=120)
    campanyname=models.CharField(max_length=202)
    empmail=models.EmailField()
    empid=models.IntegerField()
    location=models.CharField(max_length=40)
    
    