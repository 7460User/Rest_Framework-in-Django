from django.urls import path,include
from rest_framework import routers
from .models import SadiModel
from .serializers import SadiSeri
from .views import SadiView

router=routers.DefaultRouter()
router.register(r"",SadiView)

urlpatterns=[
    path("",include(router.urls))
]
