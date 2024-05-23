from rest_framework import serializers
from .models import DavidModel

class DavidSerilizer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=DavidModel
        fields='__all__'