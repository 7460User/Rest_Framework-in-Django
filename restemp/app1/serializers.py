from rest_framework import serializers
from .models import EmpModel

class EmpSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=EmpModel
        fields='__all__'
