from django import forms
from .models import ChildModels

class ChildForms(forms.Form):
    model=ChildModels
    fields='__all__'

