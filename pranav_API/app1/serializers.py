from rest_framework import serializers
from .models import Pranav_Models

class Pranav_Serial(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Pranav_Models
        fields='__all__'