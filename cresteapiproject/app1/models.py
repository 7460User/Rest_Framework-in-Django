from django.db import models

# Create your models here.
class StuModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    contact=models.IntegerField()
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name