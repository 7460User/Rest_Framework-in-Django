from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets

# Create your views here.

class Student(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

