from django.db import models

# Create your models here.
class EmpModels(models.Model):
    empname=models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.IntegerField()
    techno=models.CharField(max_length=40)
    collegename=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name
