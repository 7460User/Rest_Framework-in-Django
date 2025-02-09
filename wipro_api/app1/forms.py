from django import forms
from .models import Wipro_Model


class Wipro_forms(forms.Form):
    class Meta:
        
        model=Wipro_Model
        fields='__all__'
    