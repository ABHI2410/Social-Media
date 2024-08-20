from rest_framework import serializers
from .models import Post, Comment, Content, Vote
from user.models import Profile
from flexispace.models import FlexiSpace


class ContentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Content
        exclude = []

class PostSerializer(serializers.ModelSerializer):
    content_blocks = ContentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'flexispace', 'created_at', 'updated_at', 'content_blocks', 'upvotes', 'downvotes']
        extra_kwargs = {'upvotes': {'read_only': True}, 'downvotes': {'read_only': True}}

    
    def create(self, validated_data):
        content_data = validated_data.pop('content_blocks', [])
        post = Post.objects.create(**validated_data)
        for content in content_data:
            Content.objects.create(post=post, **content)
        return post

    def update(self, instance, validated_data):
        content_data = validated_data.pop('content_blocks', [])
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        # Update content blocks
        existing_content_ids = set(instance.content_blocks.values_list('id', flat=True))
        new_content_ids = set(content['id'] for content in content_data if 'id' in content)

        for content in content_data:
            if 'id' in content:
                content_instance = Content.objects.get(id=content['id'])
                content_instance.block_type = content.get('block_type', content_instance.block_type)
                content_instance.content_text = content.get('content_text', content_instance.content_text)
                content_instance.image_url = content.get('image_url', content_instance.image_url)
                content_instance.block_order = content.get('block_order', content_instance.block_order)
                content_instance.save()
                new_content_ids.discard(content_instance.id)
            else:
                Content.objects.create(post=instance, **content)
        
        # Delete content blocks that are no longer present
        for content_id in existing_content_ids - new_content_ids:
            Content.objects.filter(id=content_id).delete()
        
        return instance

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = Comment
        exclude = []
        extra_kwargs = {'upvotes': {'read_only': True}, 'downvotes': {'read_only': True}}


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False, allow_null=True)
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = Vote
        exclude = []
