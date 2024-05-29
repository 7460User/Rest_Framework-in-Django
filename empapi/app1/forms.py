from django import forms
from .models import EmpModels


class EmpForms(forms.Form):
    class Meta:
        model=EmpModels
        fields='__all__'
