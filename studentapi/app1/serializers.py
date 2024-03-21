from rest_framework import serializers
from .models import Student

# Creating a serializers

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields="__all__"