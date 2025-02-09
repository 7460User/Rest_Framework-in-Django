from django.urls import include,path
from .views import Wipro_Views
from .models import Wipro_Model
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',Wipro_Views)

urlpatterns = [
    path('',include(router.urls)),
]






