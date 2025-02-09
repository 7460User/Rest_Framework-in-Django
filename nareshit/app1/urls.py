from django.urls import include,path
from .views import nareshviews
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',nareshviews)


urlpatterns = [
    path("",include(router.urls)),
]