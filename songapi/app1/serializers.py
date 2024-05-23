from rest_framework import serializers
from .models import SongModel

class SongSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=SongModel
        fields='__all__'

