from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create()
            tokens = self.get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_201_CREATED)
        raise serializers.ValidationError({ 'errors': serializer.errors})

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
