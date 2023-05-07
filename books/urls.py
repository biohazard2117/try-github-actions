from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path



router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = router.urls

