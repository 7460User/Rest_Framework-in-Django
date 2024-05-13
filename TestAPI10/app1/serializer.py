from .models import EmpModels
from rest_framework import serializers

class Empserialer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=EmpModels
        fields="__all__"

    

