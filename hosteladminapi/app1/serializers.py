from rest_framework import serializers
from .models import HostelModel

class HostelSerial(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=HostelModel
        fields='__all__'