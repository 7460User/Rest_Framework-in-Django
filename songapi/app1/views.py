from django.shortcuts import render
from .models import SongModel
from .serializers import SongSerializer
from rest_framework import viewsets 

# Create your views here.

class SongData(viewsets.ModelViewSet):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializer
