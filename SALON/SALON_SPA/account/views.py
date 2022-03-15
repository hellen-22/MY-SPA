from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.models import auth

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Already taken')
                return redirect('signup')

            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')

            else:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()

                return redirect('login')

        else:
            messages.info(request, 'Password Does not match')
            return redirect('signup')
    else:
        return render(request, 'account/signup.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            print('User eists')
            return redirect('home')

        else:
            messages.info(request, 'Invalid credentials')
            print('Invalid credentials')
            return redirect('login')

    else:
        print('nothing happened')
        return render(request, 'account/login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    return render(request, 'pages/home.html')