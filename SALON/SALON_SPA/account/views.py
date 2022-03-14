from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is Taken")
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is Taken")
                return redirect('signup')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                messages.success('Account created successfully')
                return redirect('login')
    
        else:
            messages.error(request, 'Password not matching')
            return redirect('signup')

    return render(request, 'account/signup.html')