from django.shortcuts import render
from .models import Student_Model
from .serializer import Student_Serializers
from .forms import Student_Forms
from rest_framework import serializers
from rest_framework import viewsets
# Create your views here.

class Student(viewsets.ModelViewSet):
    queryset=Student_Model.objects.all()
    serializer_class=Student_Serializers

# def Student_data(request):
#     return render(request,"home_data.html")

