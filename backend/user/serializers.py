from rest_framework import serializers
from django.contrib.auth.models import User
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
    
    def get_fields(self):
        fields = super(UserSerializer, self).get_fields()
        
        if self.context.get('view').action in ['update', 'partial_update']:
            fields.pop('password')
            fields.pop('first_name')
            fields.pop('last_name')
            fields.pop('username')
            fields.pop('email')

        return fields
    
    def update(self, instance, validated_data):
        return serializers.ValidationError("User updates are not allowed.")
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)
    class Meta: 
        model = Profile
        fields = ['id', 'user', 'dob', 'bio', 'profile_picture']