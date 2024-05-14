from django.shortcuts import render
from .models import Pranav_Models
from rest_framework import viewsets
from .serializers import Pranav_Serial
# Create your views here.

class Pranav_API(viewsets.ModelViewSet):
    queryset=Pranav_Models.objects.all()
    serializer_class=Pranav_Serial