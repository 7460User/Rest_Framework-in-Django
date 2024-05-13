from django import forms
from .models import WiproEmpModel

# creating a forms code
class wiproForms(forms.Form):
    class Meta:
        models=WiproEmpModel
        fields='__all__'
        