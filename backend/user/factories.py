import factory
from django.contrib.auth.models import User
from .models import Profile
from faker import Faker
import random

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    username = factory.LazyAttribute(
        lambda o: f'{o.first_name[:random.randint(3, len(o.first_name))]}{o.last_name[:random.randint(3, len(o.last_name))]}'
    )
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    dob = factory.LazyFunction(fake.date_of_birth)
    bio = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    profile_picture = factory.django.ImageField(filename='default.svg')

# Example usage:
# user_profile = ProfileFactory()
# This will create a new User with first_name and last_name, and a related Profile object with the fake data.
