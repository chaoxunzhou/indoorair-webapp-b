from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())
        ]
    )
    last_name = serializers.CharField()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email', None)
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)

        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            request = self.context.get('request')
            login(request, user)
            return user
        else:
            raise serializers.ValidationError('Please enter valid username and password')
