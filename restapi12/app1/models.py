from django.db import models

# Create your models here.
class Student_Model(models.Model):
    name=models.CharField(max_length=20)
    companyname=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=120)
    contact=models.IntegerField()
    def __str__(self):
        return self.name

class Student_Model2(models.Model):
    techno=models.CharField(max_length=50)
    officialemail=models.CharField(max_length=40)

    def __str__(self):
        return self.name



