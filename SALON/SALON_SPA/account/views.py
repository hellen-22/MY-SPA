from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Appointment, CustomUser
from django.contrib import messages
from django.contrib.auth.models import auth
from django.views.generic import View
from .utils import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from products.models import *

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
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = 'Activate Your Account'
                message = render_to_string('registration/activate.html',
                {
                    'user' : user,
                    'domain' : current_site.domain,
                    'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                    'token' : account_activation_token.make_token(user),
                    
                }
                )
            
                email_message = EmailMessage(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                email_message.send()
                message = 'Check your email to verify your account'
                return HttpResponse(message, content_type='text/plain')
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

class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('signup')

class Password_Reset(SuccessMessageMixin, PasswordResetView):
    template_name = "passwords/password_reset.html"
    email_template_name = "passwords/password_reset_email.html"
    subject_template_name = "passwords/password_reset_subject"
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

        
def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def appointment(request):
    services = Service.objects.all()
    context = {
        services : 'services'
    }
    return render(request, "appointment/appointment.html", context)

