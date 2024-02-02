from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password',} ,write_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']
        extra_kwargs = {
        'password': {'style': {'input_type': 'password'}, 'write_only': True}
}

  
    def create(self):
        password=self.validated_data['password']
        password_confirmation=self.validated_data['confirm_password']

        if password_confirmation != password:
            raise serializers.ValidationError({'password needs to be same'})
        email = self.validated_data['email']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email already exists'})
        account=User(email=self.validated_data['email'], username=self.validated_data['username'],
                     first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])
        
        account.set_password(password)
        account.save()
        return account