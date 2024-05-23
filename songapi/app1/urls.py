from django.urls import path,include
from .models import SongModel
from .serializers import SongSerializer
from rest_framework import routers
from .views import SongData

router=routers.DefaultRouter()
router.register(r"",SongData)

urlpatterns=[
    path('',include(router.urls)),
]





