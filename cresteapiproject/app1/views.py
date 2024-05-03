from django.shortcuts import render
from .models import StuModel
from .forms import StuForm
from .serializers import StuSerializer
from rest_framework import viewsets
# Create your views here.
class StudentData(viewsets.ModelViewSet):
    queryset=StuModel.objects.all()
    serializer_class=StuSerializer

    
    
