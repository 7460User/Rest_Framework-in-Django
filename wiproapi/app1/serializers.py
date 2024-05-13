from rest_framework import serializers
from .models import WiproEmpModel

class WiproSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = WiproEmpModel
        fields = '__all__' 
