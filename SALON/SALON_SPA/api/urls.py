from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter
from knox import views as knox_views
from . views import *
from account.api import *


router = DefaultRouter()

router.register("customuser", CustomUserViewset, basename="customuser")
router.register('group', GroupViewSet, basename='group')
router.register('register', SignupViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('product', ProductViewset, basename='product')
router.register('service', ServiceViewset, basename='service')
router.register('book_appointment', BookAppointmentViewset, basename='book_appointment')


urlpatterns = router.urls