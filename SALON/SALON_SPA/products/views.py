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
