from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from flexispace.serializers import FlexiSpaceSerializer,SubscriptionSerializer
from flexispace.models import FlexiSpace,Subscription
from user.models import Profile
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import json

# View for FlexiSpace

class FlexiSpaceViewSet(viewsets.ModelViewSet):
    queryset = FlexiSpace.objects.all()
    serializer_class = FlexiSpaceSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        flexi_space = serializer.instance
        profile = Profile.objects.get(id = request.data['created_by'])
        user = profile
        Subscription.objects.create(
            user=user,
            flexispace=flexi_space
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# view for Subscription
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]