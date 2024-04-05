from rest_framework import serializers
from app1.models import Employee_Model
# I am creating a serializers
class Serializers_Employee(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee_Model
        field="__all__"

