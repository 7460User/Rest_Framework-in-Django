from django.shortcuts import render
from .models import EmpModels
from rest_framework import viewsets
from .serializers import EmpSeri
# Create your views here.

class EmpData(viewsets.ModelViewSet):
    queryset=EmpModels.objects.all()
    serializer_class=EmpSeri
    