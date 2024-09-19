from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_picture', 'followers', 'following']
        read_only_fields = ['followers', 'following']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField(label='confirm password')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("The two passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')

        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return {
            'user': user,
            'token': token.key
        }