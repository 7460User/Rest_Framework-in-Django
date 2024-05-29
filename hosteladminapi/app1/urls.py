from .models import HostelModel
from django.urls import path,include
from rest_framework import routers
from .views import Hostel_Data
from .serializers import HostelSerial

router=routers.DefaultRouter()
router.register(r"",Hostel_Data)

urlpatterns=[
    path('',include(router.urls)),
]