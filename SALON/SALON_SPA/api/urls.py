from cgitb import lookup
from itertools import product
from django.urls import path, include
from . import views
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from knox import views as knox_views
from . views import *
from account.api import *


router = DefaultRouter()

router.register("customuser", CustomUserViewset, basename="customuser")
router.register('group', GroupViewSet, basename='group')
router.register('register', SignupViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('categories', views.CategoryViewSet)
router.register('product', views.ProductViewset, basename='product')
router.register('service', ServiceViewset, basename='service')
router.register('book_appointment', BookAppointmentViewset, basename='book_appointment')
router.register('cart', views.CartViewSet, basename='cart')

cart_item_router = NestedDefaultRouter(router, 'cart', lookup='cart')
cart_item_router.register('items', views.CartItemViewSet, basename='items')

urlpatterns = router.urls + cart_item_router.urls