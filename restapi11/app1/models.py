from django.db import models

# Create your models here.

class EmpModels(models.Model):
    name = models.CharField(max_length=20)
    technology = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)  
    contact = models.CharField(max_length=15)  
    location = models.CharField(max_length=30)
    address = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

