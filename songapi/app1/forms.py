from django import forms
from .models import SongModel

class SongForm(forms.Form):
    class Meta:
        model=SongModel
        fields='__all__'