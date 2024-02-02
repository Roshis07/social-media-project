from django.contrib.auth.models import User
from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create()
            tokens = self.get_tokens_for_user(user)

            return Response({'success': True,'tokens': tokens})
            
        return Response({'success': False})   

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
