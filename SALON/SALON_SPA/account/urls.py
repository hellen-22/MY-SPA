from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]