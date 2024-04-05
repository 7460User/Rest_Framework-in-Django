from django import forms
from .models import UserProfile

class PhoneVerificationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number']

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6)
