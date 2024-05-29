from .models import ChildModels
from .serializers import ChildSeri 
from django.urls import path,include
from .views import ChildView
from  rest_framework import routers

router=routers.DefaultRouter()
router.register(r"",ChildView)

urlpatterns=[
    path('',include(router.urls)),
]