from django.shortcuts import render
from .models import SadiModel
from .serializers import SadiSeri
from rest_framework import viewsets
# Create your views here.

class SadiView(viewsets.ModelViewSet):
    queryset=SadiModel.objects.all()
    serializer_class=SadiSeri