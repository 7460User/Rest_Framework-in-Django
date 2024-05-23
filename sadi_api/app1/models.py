from django.db import models

# Create your models here.
class SadiModel(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    date=models.DateField()
    contact=models.IntegerField()
    location=models.CharField(max_length=120)
    district=models.CharField(max_length=20)

    def __str__(self):
        return self.name
