from django.db import models
# Create your models here.

class StudentModels(models.Model):
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=120)
    