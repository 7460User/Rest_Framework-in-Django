from django import forms
from .models import Pranav_Models

class Pranav_Forms(forms.Form):
    class Meta:
        model=Pranav_Models
        fields='__all__'