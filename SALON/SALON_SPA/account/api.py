from rest_framework import generics, permissions, serializers
from api.serializers import *
from knox.models import AuthToken
from rest_framework.response import Response

class SignUpAPI(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            'users': CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'token' : token[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user':CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(user)[1]
        })