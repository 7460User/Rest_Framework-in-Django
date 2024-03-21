from django.urls import path,include
from app1.views import Student
from rest_framework import routers

# Creating a urls

router=routers.DefaultRouter()
router.register(r'',Student)

urlpatterns = [
    path('',include(router.urls))
]