from django.shortcuts import render
from .admin import WiproEmpModel
from .serializers import WiproSerializer
# from .forms import wiproForms
from rest_framework import viewsets
# Create your views here.

class StudentData(viewsets.ModelViewSet):
    queryset = WiproEmpModel.objects.all()
    serializer_class = WiproSerializer
    


