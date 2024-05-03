from .admin import StuModel
from rest_framework import serializers

# Define the serializer class
class StuSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StuModel  
        fields = '__all__'
