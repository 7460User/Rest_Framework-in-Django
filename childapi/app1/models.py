from django.db import models

# Create your models here.
class ChildModels(models.Model):
    name=models.CharField(max_length=30)
    sname=models.CharField(max_length=30)
    age=models.IntegerField()
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    