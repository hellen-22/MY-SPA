from unicodedata import name
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),

]