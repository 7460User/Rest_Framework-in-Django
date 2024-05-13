from django.shortcuts import render
from .models import EmpModels
from .serializer import Empserialer
from .forms import EmpForms
from rest_framework import viewsets
# Create your views here.

class Student_View(viewsets.ModelViewSet):
    queryset=EmpModels.objects.all()
    serializer_class=Empserialer