from django import forms
from .models import EmpModels

class EmpForms(forms.Form):
    class Meta:
        models=EmpModels
        fields="__all__"