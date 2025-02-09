from django.db import models

# Create your models here.

class Nareshit(models.Model):
    name=models.CharField(max_length=30)
    teachername=models.CharField(max_length=40)
    teachersalary=models.IntegerField()
    subject=models.CharField(max_length=40)
    