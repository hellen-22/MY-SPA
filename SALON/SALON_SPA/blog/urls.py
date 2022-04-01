from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('blog/', views.blog, name='blog'),

]