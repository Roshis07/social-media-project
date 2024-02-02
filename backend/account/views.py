from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

@api_view(['POST'])
def custom_logout(request):
    try:
        request.auth.delete()  # Invalidate the token
    except AttributeError:
        pass  # If the token is not present, do nothing
    return Response({'detail': 'Successfully logged out.'})
