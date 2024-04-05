from django.shortcuts import render,redirect
from django.views import View
from .models import Employee_Model
from rest_framework import viewsets
from app1.serializers import Serializers_Employee
from app1.forms import EmployeeForm

# Create your views here.

class Employee_Data(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            cname = request.POST.get('cname')
            salary = request.POST.get('salary')
            
            employee = Employee_Model(name=name, email=email, cname=cname, salary=salary)
            employee.save()
            return redirect('/data')
    
        return render(request, 'home.html')

def get_data(request):
    serviceData=Employee_Model.objects.all()
    data={
        'serviceData': serviceData
    }
    return render(request,"data.html",data)

def Delete_data(request,id):
    student=Employee_Model.objects.get(id=id)
    student.delete()
    return redirect('/data')
    

def update_data(request, id):
    pass
