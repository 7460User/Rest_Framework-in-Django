from .models import DavidModel
from .serializers import DavidSerilizer
from django.urls import path,include
from .views import David_API
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"",David_API)

urlpatterns=[
    path('',include(router.urls)),
]