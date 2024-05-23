from django.db import models
# Create your models here.
class SongModel(models.Model):
    singername=models.CharField(max_length=30)
    sage=models.IntegerField()
    slocation=models.CharField(max_length=100)
    semail=models.EmailField()
    scontact=models.IntegerField()
    songname=models.CharField(max_length=120)

    def __str__(self):
        return self.singername
   