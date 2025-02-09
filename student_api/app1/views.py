from django.shortcuts import render
from .models import StudentModels
from rest_framework import viewsets
from .serializer import StudentSerializer
# Create your views here.

class Student_data(viewsets.ModelViewSet):
    queryset=StudentModels.objects.all()
    serializer_class=StudentSerializer