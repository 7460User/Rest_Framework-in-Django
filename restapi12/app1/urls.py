from .models import Student_Model
from .forms import Student_Forms
from .serializer import Student_Serializers
from .views import Student
# from .views import Student_data
from django.urls import path,include
from rest_framework import routers

# creating a router in url

router=routers.DefaultRouter()
router.register(r'',Student)
# router.register(r'home',Student_data)
urlpatterns=[
    path('',include(router.urls)),
    # path('home',include(router.urls)),
]