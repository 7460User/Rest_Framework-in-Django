from django import forms
from .models import EmpModel

class EmpForms(forms.Form):
    class Meta:
        models=EmpModel
        fields='__all__'
        