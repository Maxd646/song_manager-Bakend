from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'api/songs', SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]

