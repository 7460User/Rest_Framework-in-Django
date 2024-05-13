from .models import EmpModels
from django.urls import include,path
from .views import Govind_API
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'',Govind_API)

urlpatterns=[
    path("",include(router.urls))
]