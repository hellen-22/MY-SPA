from unicodedata import name
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.products, name='products'),
    path('cart/', views.add_cart, name='add-cart'),

    # Cart Item urls
    path('cart-item-list/', CartItemList.as_view(), name='cartitem_list'),
    path('add-cart-item/', CartItemCreateView.as_view(), name='add_cartitem'),
    path('<pk>/update', CartItemUpdateView.as_view(), name='update_cartitem'),
    path('<pk>/delete', CartItemDeleteView.as_view(), name='delete_cartitem'),

]