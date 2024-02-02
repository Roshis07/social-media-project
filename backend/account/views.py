from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token),
                }, status=status.HTTP_201_CREATED)

        raise serializers.ValidationError({ 'errors': serializer.errors}, code=status.HTTP_400_BAD_REQUEST)
