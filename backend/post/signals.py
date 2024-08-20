from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Vote

@receiver(post_save, sender=Vote)
def update_vote_count_on_create(sender, instance, **kwargs):
    if instance.post:
        post = instance.post
        upvotes = post.votes.filter(vote_type=1).count()
        downvotes = post.votes.filter(vote_type=0).count()
        post.upvotes = upvotes
        post.downvotes = downvotes
        post.save()
    elif instance.comment:
        comment = instance.comment
        upvotes = comment.votes.filter(vote_type=1).count()
        downvotes = comment.votes.filter(vote_type=0).count()
        comment.upvotes = upvotes
        comment.downvotes = downvotes
        comment.save()

@receiver(post_delete, sender=Vote)
def update_vote_count_on_delete(sender, instance, **kwargs):
    if instance.post:
        post = instance.post
        upvotes = post.votes.filter(vote_type=1).count()
        downvotes = post.votes.filter(vote_type=0).count()
        post.upvotes = upvotes
        post.downvotes = downvotes
        post.save()
    elif instance.comment:
        comment = instance.comment
        upvotes = comment.votes.filter(vote_type=1).count()
        downvotes = comment.votes.filter(vote_type=0).count()
        comment.upvotes = upvotes
        comment.downvotes = downvotes
        comment.save()
