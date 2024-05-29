from .models import HostelModel
from django import forms

class HotelForms(forms.Form):
    class Meta:
        model=HostelModel
        fields='__all__'
        