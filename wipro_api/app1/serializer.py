from rest_framework import serializers
from .models import Wipro_Model

class WiproSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Wipro_Model
        fields='__all__'
        