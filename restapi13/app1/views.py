from django.shortcuts import render
from .models import StudentModels
from .serializers import EmpSerialer
from rest_framework import viewsets

# Create your views here.

class Student_Data(viewsets.ModelViewSet):
    queryset=StudentModels.objects.all()
    serializer_class=EmpSerialer