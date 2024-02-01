from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password and confirm password do not match.")
        return data
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().create(validated_data)
        return instance