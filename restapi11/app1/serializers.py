from rest_framework import serializers
from .models import EmpModels

class EmpSerialer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmpModels  
        fields = '__all__'


