from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """

    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def validate(self, attrs):
        """
        Validate input data before creating a new User instance.
        """
        # Validate username uniqueness
        username = attrs.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username is already taken.'})

        # Validate email uniqueness
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email address is already registered.'})

        # Validate first_name and last_name are strings without numeric digits
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not isinstance(first_name, str) or not first_name.isalpha():
            raise serializers.ValidationError({'first_name': 'First name should be a valid string without numeric digits.'})

        if not isinstance(last_name, str) or not last_name.isalpha():
            raise serializers.ValidationError({'last_name': 'Last name should be a valid string without numeric digits.'})

        # Validate first_name and last_name length
        if len(first_name.strip()) == 0:
            raise serializers.ValidationError({'first_name': 'First name cannot be empty.'})
        if len(last_name.strip()) == 0:
            raise serializers.ValidationError({'last_name': 'Last name cannot be empty.'})
        if len(first_name) > 30:
            raise serializers.ValidationError({'first_name': 'First name must be 30 characters or fewer.'})
        if len(last_name) > 30:
            raise serializers.ValidationError({'last_name': 'Last name must be 30 characters or fewer.'})

        # You can add more custom validation logic here if needed

        return attrs

    def create(self, validated_data):
        """
        Create and return a new User instance.
        """
        user = User.objects.create_user(**validated_data)
        return user

    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username/password.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data
