from rest_framework import serializers
from .models import StudentModels

class EmpSerialer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = StudentModels 
        fields = '__all__'