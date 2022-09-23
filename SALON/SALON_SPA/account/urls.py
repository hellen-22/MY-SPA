from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('home-approved/', views.homeApproved, name='home-approved'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path("password_reset/", Password_Reset.as_view(), name="password_reset"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('appointment/', views.appointment, name='appointment'),
    path('success/', views.success_book, name='success'),
]