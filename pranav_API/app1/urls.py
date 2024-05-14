from .models import Pranav_Models
from .serializers import Pranav_Serial
from django.urls import path,include
from .views import Pranav_API
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'',Pranav_API)

urlpatterns=[
    path('',include(router.urls)),
]