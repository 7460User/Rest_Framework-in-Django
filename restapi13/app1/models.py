from django.db import models

# Create your models here.

class StudentModels(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    roll=models.IntegerField()
    contact=models.IntegerField()
    address=models.CharField(max_length=140)

    def __str__(self):
        return self.name
    
