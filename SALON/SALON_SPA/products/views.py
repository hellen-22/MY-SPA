from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products.html', context)

@login_required
def services(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, 'services.html', context) 
