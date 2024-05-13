from django.db import models

# Create your models here.

class EmpModels(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    district=models.CharField(max_length=30)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name


