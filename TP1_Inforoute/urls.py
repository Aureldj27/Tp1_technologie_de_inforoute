from django.urls import path, include
from rest_framework import routers
from .views import DatasetViewSet

router = routers.DefaultRouter()
router.register(r'datasets', DatasetViewSet, basename='dataset')

urlpatterns = [
    path('api/', include(router.urls)),
]