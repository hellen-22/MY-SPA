from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]