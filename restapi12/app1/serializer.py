from rest_framework import serializers
from .models import Student_Model

# creating a serializers 
class Student_Serializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Student_Model
        fields='__all__'

