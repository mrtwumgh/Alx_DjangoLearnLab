from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_picture', 'followers', 'following']
        read_only_fields = ['followers', 'following']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label='confirm password')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("The two passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')

        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        token, created = Token.objects.get_or_create(user=user)
        return {
            'user': user,
            'token': token.key
        }