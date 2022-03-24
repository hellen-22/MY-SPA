from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')