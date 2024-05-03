from .models import StuModel
from .forms import StuForm
from .serializers import StuSerializer
from .views import StudentData
from rest_framework import routers
from django.urls import path,include

# write a urls code 

router=routers.DefaultRouter()
router.register(r'',StudentData)

urlpatterns=[
    path('',include(router.urls)),
]