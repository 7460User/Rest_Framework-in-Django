from django.db import models
# Create your models here.

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
