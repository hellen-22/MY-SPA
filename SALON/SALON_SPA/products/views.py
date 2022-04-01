from pyexpat import model
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

# Create your views here.

def products(request):
    return render(request, 'products.html')
"""
def cart(request):
    return render(request, 'cart.html')
"""
def add_cart(request):
    return redirect('cart_itemlist')
# Cart class
class CartCreateView(CreateView):
    model = Cart
    fields = '__all__'
    template_name = 'cart/add_cart.html'

# Cart List class
class CartItemCreateView(CreateView):
    model = CartItem
    fields = '__all__'
    template_name = 'cart-item/add_cart_item.html'
    success_url = reverse_lazy('cartitem_list')

class CartItemList(ListView):
    model = CartItem
    template_name = 'cart-item/cart_item.html'

class CartItemUpdateView(UpdateView):
    model = CartItem
    fields = '__all__'
    template_name = 'cart-item/update_cartitem.html'

class CartItemDeleteView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('products')
