from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=80)
    mobile=models.IntegerField()
    address=models.CharField(max_length=120)
    about=models.CharField(max_length=120)
    date=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name