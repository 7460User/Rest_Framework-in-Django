from rest_framework import routers
from django.urls import include, path
from .views import Student_View

router = routers.DefaultRouter()
router.register(r'', Student_View)

urlpatterns = [
    path('', include(router.urls))  # Change "router.urls" instead of "router"
]
