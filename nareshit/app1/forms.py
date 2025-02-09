from djando import forms
from models import Nareshit

class nareshitforms(forms.Form):
    class Meta:
        model=Nareshit
        fields='__all__'
        