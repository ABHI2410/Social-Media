from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Subscription


# Defining signals to update number of subscribers when ever someone subscribes or unsubscribes

@receiver(post_save, sender=Subscription)
def update_subscription_count_on_create(sender, instance, **kwargs):
    flexi_space = instance.flexispace
    flexi_space.no_of_subscriptions = flexi_space.subscribed_to.count()
    flexi_space.save()

@receiver(post_delete, sender=Subscription)
def update_subscription_count_on_delete(sender, instance, **kwargs):
    flexi_space = instance.flexispace
    flexi_space.no_of_subscriptions = flexi_space.subscribed_to.count()
    flexi_space.save()
