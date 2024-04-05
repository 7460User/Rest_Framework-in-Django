from django import forms
from .models import Employee_Model

# creating a forms
class EmployeeForm(forms.Form):
    class Meta:
        model=Employee_Model
        fields="__all___"