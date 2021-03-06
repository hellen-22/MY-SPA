from decimal import Decimal
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Product


def get_user_cart(request):
    cart_id = None
    cart = None
    # If the user is logged in, then grab the user's cart info.
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart(user=request.user)
            cart.save()
    else:
        cart_id = request.session.get('cart_id')
        if not cart_id:
            cart = Cart()
            cart.save()
            request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.get(id=cart_id)
    return cart


def view_cart(request):
    cart = get_user_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    order_total = Decimal(0.0)
    for item in cart_items:
        order_total += (item.product.price * item.quantity)
    context = {
        'cart_items':cart_items
    }
    return render(request, 'view_cart.html', context)

def get_cart_count(request):
    cart = get_user_cart(request)
    total_count = 0
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        total_count += item.quantity
    return total_count


def update_cart_info(request):
    request.session['cart_count'] = get_cart_count(request)



def add_to_cart(request, slug):
    cart = get_user_cart(request)
    product = Product.objects.get(slug=slug)
    quantity = int(request.POST.get('qty')) or 1
    cart_item = CartItem(product=product, cart=cart, quantity=0)
    cart_item.quantity += quantity
    cart_item.save()
    if request.session.get('cart_count'):
        request.session['cart_count'] += quantity
    else:
        request.session['cart_count'] = quantity
    update_cart_info(request)
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    quantity = cart_item.quantity
    cart_item.delete()
    if request.session.get('cart_count'):
        request.session['cart_count'] -= quantity
    else:
        request.session['cart_count'] = 0
    update_cart_info(request)
    return redirect(reverse('view_cart'))