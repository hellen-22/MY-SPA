from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add-cart/', views.add_to_cart, name='add-cart')

]