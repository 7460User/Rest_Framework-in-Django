from rest_framework import serializers
from .models import Nareshit

class nareshserializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Nareshit
        fields='__all__'
