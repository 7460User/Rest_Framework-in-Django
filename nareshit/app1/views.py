from django.shortcuts import render
from .models import Nareshit
from rest_framework import viewsets
from .serializer import nareshserializer
# Create your views here.

class nareshviews(viewsets.ModelViewSet):
    queryset=Nareshit.objects.all()
    serializer_class=nareshserializer
    
