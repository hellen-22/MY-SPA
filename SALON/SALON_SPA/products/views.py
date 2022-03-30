from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def products(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')
@login_required
def add_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    cart.add_to_cart (product_id)
    return redirect('cart')
