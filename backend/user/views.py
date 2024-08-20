from user.models import Profile
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from user.serializers import ProfileSerializer, RegisterSerializer, LoginSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics
import json

# View to perform CRUD on User and profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data.get('user')
        serializer.data.pop('user')
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        user.set_password(request.data['user.password'])
        user.save()

        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            file_path = default_storage.save(f"profilePicture/{profile_picture.name}", ContentFile(profile_picture.read()))
        else:
            file_path = 'media/profilePicture/default.svg'

        # # Create Profile
        profile = Profile(
            user=user,
            dob=serializer.data.get('dob'),
            bio=serializer.data.get('bio', ''),
            profile_picture=file_path
        )
        
        profile.save()

        serializer = ProfileSerializer(profile, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()        
        profile_picture = request.FILES.get('profile_picture')

        # Update profile instance
        if profile_picture:
            file_path = default_storage.save(f"profilePicture/{profile_picture.name}", ContentFile(profile_picture.read()))
            instance.profile_picture = file_path
        instance.dob = request.data.get('dob', instance.dob)
        instance.bio = request.data.get('bio', instance.bio)
        instance.profile_picture = file_path if profile_picture else instance.profile_picture

        instance.save()
        # Return serialized profile
        serializer = ProfileSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)