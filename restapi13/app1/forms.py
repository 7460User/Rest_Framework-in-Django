from django import forms
from .models import StudentModels


class EmpForms(forms.Form):
    class Meta:
        model=StudentModels
        fields="__all__"