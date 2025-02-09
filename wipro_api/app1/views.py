from django.shortcuts import render
from .models import Wipro_Model
from rest_framework import serializers
from rest_framework import viewsets
from .serializer import WiproSerializer
# Create your views here.
class Wipro_Views(viewsets.ModelViewSet):
    queryset=Wipro_Model.objects.all()
    serializer_class=WiproSerializer
