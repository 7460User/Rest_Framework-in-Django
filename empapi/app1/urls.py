from .models import EmpModels 
from rest_framework import routers
from .views import EmpData
from django.urls import path,include

router=routers.DefaultRouter()
router.register(r'',EmpData)

urlpatterns=[
    path('',include(router.urls)),
]