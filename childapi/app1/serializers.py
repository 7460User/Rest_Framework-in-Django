from rest_framework import serializers
from app1.models import ChildModels

class ChildSeri(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=ChildModels
        fields='__all__'
        