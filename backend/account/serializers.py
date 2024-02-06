from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password',} ,write_only=True)

    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only': True}
            }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password=validated_data['password']
        confirm_password=validated_data['confirm_password']

        if confirm_password != password:
            raise serializers.ValidationError({'password': 'Password needs to be same'})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email already exists'})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username already exists'})

        account=User(email=email, username=username,
                     first_name=validated_data['first_name'], last_name=validated_data['last_name'])

        account.set_password(password)
        account.save()

        return account
