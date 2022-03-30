from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.products, name='products'),
    path('cart/', views.cart, name='cart')
]