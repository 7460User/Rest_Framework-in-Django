from django.shortcuts import render
from .models import EmpModel
from .serializers import EmpSerializer
from .forms import EmpForms
from rest_framework import viewsets
# Create your views here.

class EmpData(viewsets.ModelViewSet):
    queryset=EmpModel.objects.all()
    serializer_class=EmpSerializer
