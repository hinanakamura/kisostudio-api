from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, ProductViewSet, ImageViewSet

router = DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"image", ImageViewSet)
app_name = "ec"
urlpatterns = [
    path("", include(router.urls))
    ]