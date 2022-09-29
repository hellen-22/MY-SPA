from django.contrib.auth.models import Group
from rest_framework import serializers, viewsets, permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from account.models import CustomUser, Appointment
from products.models import *
from .serializers import *

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer 
    permission_class = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]

class SignupViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer
    permission_class = [permissions.IsAuthenticated]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer
    permission_class = [permissions.IsAuthenticated]

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    permission_class = [permissions.IsAuthenticated]

class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer 
    permission_class = [permissions.IsAuthenticated]

class BookAppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(CreateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer