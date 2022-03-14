from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password 


    return render(request, 'account/signup.html')