from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StationDataViewSet

router = DefaultRouter()
router.register(r'stationdata', StationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
