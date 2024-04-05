from django.db import models

# Create your models here.
class Employee_Model(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=70)
    cname=models.CharField(max_length=50)
    salary=models.IntegerField()

    def __str__(self):
        return self.name