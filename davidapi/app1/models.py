from django.db import models

# Create your models here.

class DavidModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    village=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    location=models.CharField(max_length=110)
    