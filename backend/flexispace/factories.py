import factory
from user.models import Profile
from user.factories import ProfileFactory
from .models import FlexiSpace, Subscription
from faker import Faker

fake = Faker()

class FlexiSpaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FlexiSpace

    name = factory.Sequence(lambda n: f'FlexiSpace{n}')
    description = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))
    created_by = factory.SubFactory(ProfileFactory)
    created_at = factory.LazyFunction(fake.date_time_this_decade)
    updated_at = factory.LazyFunction(fake.date_time_this_decade)
    no_of_subscriptions = factory.LazyFunction(lambda: fake.random_int(min=0, max=100))

class SubscriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscription

    user = factory.SubFactory(ProfileFactory)
    flexispace = factory.SubFactory(FlexiSpaceFactory)
    created_at = factory.LazyFunction(fake.date_time_this_decade)

# Example usage:
# flexispace = FlexiSpaceFactory()
# subscription = SubscriptionFactory(user=profile_instance, flexispace=flexispace_instance)
