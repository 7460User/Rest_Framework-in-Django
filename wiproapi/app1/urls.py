from .models import WiproEmpModel
from django.urls import path,include
from .views import StudentData
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'',StudentData)

urlpatterns=[
    path('',include(router.urls))
]