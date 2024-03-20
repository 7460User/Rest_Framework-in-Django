from rest_framework import serializers
from .models import Company
from .models import Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'  



#Employee serializers

class EmployeeSerializeri(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"
