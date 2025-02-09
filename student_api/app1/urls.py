from django.urls import path,include
from .models import StudentModels
from  rest_framework import routers
from .views import Student_data

router=routers.DefaultRouter()
router.register(r'',Student_data)

urlpatterns=[
    path('',include(router.urls)),
]
