from .models import StudentModels
from .views import Student_Data
from django.urls import path,include
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"",Student_Data)

urlpatterns=[
    path('',include(router.urls)),

]
