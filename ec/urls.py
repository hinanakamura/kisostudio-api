from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, ProductViewSet, ImageViewSet, AuthRegister,AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView
# from .views import CategoryViewSet, ProductViewSet, ImageViewSet, UserViewSet, AuthRegister,AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView


router = DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"image", ImageViewSet)
# router.register(r"user", UserViewSet)
router.register(r"register", AuthRegister)
router.register(r"mypage", AuthInfoGetView)
router.register(r"auth_update", AuthInfoUpdateView)
router.register(r"delete", AuthInfoDeleteView)
from rest_framework_jwt.views import obtain_jwt_token
app_name = "ec"
urlpatterns = [
    path("", include(router.urls)),
    path("mail", views.send_email),

    path('login/', obtain_jwt_token),
    ]