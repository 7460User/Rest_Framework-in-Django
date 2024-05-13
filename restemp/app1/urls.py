from .models import EmpModel
from .forms import EmpForms
from .serializers import EmpSerializer
from rest_framework import routers
from django.urls import path,include
from .views import EmpData

router=routers.DefaultRouter()
router.register(r'',EmpData)

urlpatterns=[
    path('',include(router.urls))
]