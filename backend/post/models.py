from django.db import models
from user.models import Profile
from flexispace.models import FlexiSpace
from django.core.exceptions import ValidationError

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    flexispace = models.ForeignKey(FlexiSpace, on_delete=models.CASCADE, related_name='posts')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='content_blocks')
    block_type = models.CharField(max_length=10, choices=[('text', 'Text'),('image', 'Image'),])
    content_text = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to="media/FlexiSpacePicture",null=True, blank=True)
    block_order = models.PositiveIntegerField()

    class Meta:
        ordering = ['block_order']

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='votes')
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, related_name='votes')
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.BooleanField(choices=[(1, 'Upvote'), (0, 'Downvote'),])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'post', 'comment')
    
    def clean(self):
        if not self.post and not self.comment:
            raise ValidationError('Either post or comment must be provided.')
        if self.post and self.comment:
            raise ValidationError('Cannot specify both post and comment.')

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method to perform validation
        super().save(*args, **kwargs)