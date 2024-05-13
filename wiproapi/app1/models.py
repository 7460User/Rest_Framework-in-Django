from django.db import models

# Create your models here.
class WiproEmpModel(models.Model):
    empname=models.CharField(max_length=20)
    ofclemail=models.CharField(max_length=30)
    techno=models.CharField(max_length=30)
    age=models.IntegerField()
    complocation=models.CharField(max_length=40)

    def __str__(self):
        return self.name