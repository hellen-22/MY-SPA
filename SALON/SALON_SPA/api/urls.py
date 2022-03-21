from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter
from account.api import *
from knox import views as knox_views

router = DefaultRouter()

router.register("customuser", CustomUserViewset, basename="customuser")
router.register('group', GroupViewSet, basename='group')
router.register('register', SignupViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')


urlpatterns = [
    path("", include(router.urls)),
    #API endpoints
    path('auth/', include('knox.urls')),
    path('auth/register', SignUpAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name='knox-logout')
]