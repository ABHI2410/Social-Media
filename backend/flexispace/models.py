from django.db import models
from user.models import Profile

# FlexiSpace Model 
# add any additional field for Flexispace here
class FlexiSpace(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True,blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='flexispace_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    no_of_subscriptions = models.PositiveIntegerField(default=0)

# Subscription Model
# Model to keep track of users subscribed to different FlexiSpace.
class Subscription(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='subscribed_by')
    flexispace = models.ForeignKey(FlexiSpace, on_delete=models.CASCADE, related_name='subscribed_to')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'flexispace')