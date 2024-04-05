from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import PhoneVerificationForm, OTPVerificationForm
from .models import UserProfile
import random


def send_otp(phone_number):
   
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    print(f"OTP for {phone_number}: {otp}")
    return otp

def verify_phone(request):
    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            otp = send_otp(phone_number)
            UserProfile.objects.update_or_create(phone_number=phone_number, defaults={'otp': otp})
            request.session['phone_number'] = str(phone_number)
            return redirect('verify_otp')
    else:
        form = PhoneVerificationForm()
    return render(request, 'verify_phone.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            phone_number = request.session.get('phone_number')
            user_profile = UserProfile.objects.filter(phone_number=phone_number, otp=otp).first()
            if user_profile:
                login(request, user_profile)
                return redirect('home')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
    else:
        form = OTPVerificationForm()
    return render(request, 'verify_otp.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('verify_phone')
