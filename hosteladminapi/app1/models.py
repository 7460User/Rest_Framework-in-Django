from django.db import models

# Create your models here.
class HostelModel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.name