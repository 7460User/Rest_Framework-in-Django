from rest_framework import serializers
from app1.models import SadiModel

class SadiSeri(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=SadiModel
        fields='__all__'