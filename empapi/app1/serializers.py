from rest_framework import serializers
from .models import EmpModels

class EmpSeri(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=EmpModels
        fields='__all__'