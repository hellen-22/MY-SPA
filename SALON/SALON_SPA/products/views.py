from django.shortcuts import redirect, render, get_object_or_404
from matplotlib.style import context
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy


# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products.html', context)
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

    def cart_item(request):
        items = CartItem.objects.all()
        context = {
            'items':items
        }
        return render(request, context)

class CartItemUpdateView(UpdateView):
    model = CartItem
    fields = '__all__'
    template_name = 'cart-item/update_cartitem.html'

class CartItemDeleteView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('products')
