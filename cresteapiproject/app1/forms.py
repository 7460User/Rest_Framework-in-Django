from django import forms
from .models import StuModel
# from .serializers import StuSerializer

# creating a forms code
class StuForm(forms.Form):
    class Meta:
        models=StuModel
        fields='__all__'