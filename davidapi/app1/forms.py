from django import forms
from app1.models import DavidModel

class DavidForms(forms.Form):
    class Meta:
        models=DavidModel
        fields="__all__"