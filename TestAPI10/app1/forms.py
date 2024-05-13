from .models import EmpModels
from django import forms

class EmpForms(forms.Form):
    class Meta:
        models=EmpModels
        fields="__all__"
        