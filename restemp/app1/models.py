from django.db import models

class EmpModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    contact = models.IntegerField()
    development = models.CharField(max_length=120)
    locations = models.CharField(max_length=120)
    sector = models.CharField(max_length=50, null=True, blank=True)  # Make sector nullable
    
    def __str__(self):
        return self.name

