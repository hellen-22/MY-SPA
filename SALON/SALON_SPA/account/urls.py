from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("password_reset/", Password_Reset.as_view(), name="password_reset"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]