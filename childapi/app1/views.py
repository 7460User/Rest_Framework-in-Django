from django.shortcuts import render
from .models import ChildModels
from .serializers import ChildSeri
from rest_framework import viewsets
# Create your views here.

class ChildView(viewsets.ModelViewSet):
    queryset=ChildModels.objects.all()
    serializer_class=ChildSeri
    