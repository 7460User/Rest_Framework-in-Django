from django import forms
from app1.models import SadiModel

class SadiForms(forms.Form):
    class Meta:
        model=SadiModel
        fields='__all__'

