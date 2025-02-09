from djando import forms
from .models import StudentModels

class StudentForms(forms.Forms):
    class Meta:
        model=StudentModels
        fields='__all__'
        
