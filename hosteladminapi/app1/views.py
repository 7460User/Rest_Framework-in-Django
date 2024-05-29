from django.shortcuts import render
from .models import HostelModel
from .serializers import HostelSerial
from rest_framework import viewsets
# Create your views here.
class Hostel_Data(viewsets.ModelViewSet):
    queryset=HostelModel.objects.all()
    serializer_class=HostelSerial
