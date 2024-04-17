from django import forms
from app1.models import Student_Model

class Student_Forms(forms.Form):
    class Meta:
        model=Student_Model
        fields="__all__"
