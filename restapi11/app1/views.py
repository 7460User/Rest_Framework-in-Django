from django.shortcuts import render
from rest_framework import viewsets
from .models import EmpModels
from .serializers import EmpSerialer
# Create your views here.

class Govind_API(viewsets.ModelViewSet):
    queryset=EmpModels.objects.all()
    serializer_class=EmpSerialer
