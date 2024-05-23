from django.shortcuts import render
from .models import DavidModel
from .serializers import DavidSerilizer
from rest_framework import viewsets
# Create your views here.

class David_API(viewsets.ModelViewSet):
    queryset = DavidModel.objects.all()
    serializer_class = DavidSerilizer
