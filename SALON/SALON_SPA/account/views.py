from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def signup(request):
    
    return render(request, 'account/signup.html')