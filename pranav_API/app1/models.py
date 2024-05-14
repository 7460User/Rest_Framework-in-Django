from django.db import models

# Create your models here.

class Pranav_Models(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    mob=models.IntegerField()
    email=models.CharField(max_length=40)
    location=models.CharField(max_length=101)