import re
from datetime import datetime, date

from rest_framework import serializers

from flexispace.models import FlexiSpace,Subscription
from user.models import Profile


# Serializer for Flexispace for CRUD and validating 
# Write data validation here and field access control for API. 
# please write validation 
class FlexiSpaceSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)
    class Meta:
        model = FlexiSpace
        exclude = ['updated_at']
        extra_kwargs = {'no_of_subscriptions': {'read_only': True}}


# Serializer for Flexispace for CRUD
class SubscriptionSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)
    flexispace =  serializers.PrimaryKeyRelatedField(queryset=FlexiSpace.objects.all(), write_only=True)
    class Meta:
        model = Subscription
        exclude = []