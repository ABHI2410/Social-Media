from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from user.models import Profile
import re
from datetime import datetime, date


## User serializer for CRUD and validating 
## Write data validation here and field access control for API.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email', 'first_name', 'last_name', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True, 'required': True, 'style':{'input_type': 'password'}},
                        'date_joined': {'read_only': True}}
    
    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Username should only contain letters and numbers.")
        return value

    def validate_first_name(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("First name should only contain letters or spaces.")
        return value

    def validate_last_name(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("Last name should only contain letters or spaces.")
        return value

    def validate_email(self, value):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, value):
            raise serializers.ValidationError("Invalid email address.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or len(value) > 25:
            raise serializers.ValidationError("Password must be between 8 and 25 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one numeric character.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase character.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase character.")
        special_characters = set('''!@#$%^&*()_+{}<>?|[]\\;',./:"''')
        if not special_characters.intersection(value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value
    
    def update(self, instance, validated_data):
        return serializers.ValidationError("User updates are not allowed.")
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only = True)
    class Meta: 
        model = Profile
        fields = ['id', 'user', 'dob', 'bio', 'profile_picture']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    tokens = serializers.SerializerMethodField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials.')
        tokens = self.get_tokens_for_user(user)
        return {'tokens': tokens}

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }