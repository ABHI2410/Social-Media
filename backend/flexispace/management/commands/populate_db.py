from django.core.management.base import BaseCommand
from user.models import Profile
from flexispace.models import FlexiSpace, Subscription
from post.models import Post, Content, Comment, Vote
from user.factories import ProfileFactory
from flexispace.factories import FlexiSpaceFactory, SubscriptionFactory
from post.factories import PostFactory, ContentFactory, CommentFactory, VoteFactory
import random
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Populate the database with sample data if it is empty'

    def handle(self, *args, **kwargs):
        if Profile.objects.exists():
            self.stdout.write(self.style.WARNING('Database is already populated.'))
            return

        self.stdout.write(self.style.NOTICE('Populating database...'))

        users = []
        profiles = [ProfileFactory.create() for _ in tqdm(range(10), desc="Creating Profiles")]

        for profile in tqdm(profiles, desc="Processing Profiles"):
            # Create varying numbers of FlexiSpaces
            for _ in range(random.randint(1, 10)):
                flexispace = FlexiSpaceFactory.create(created_by=profile)

                subscribed_profiles = [profile]

                # Create subscriptions with different profiles
                for _ in range(random.randint(1, 8)):
                    # Exclude profiles already subscribed to this FlexiSpace
                    available_profiles = [p for p in profiles if p not in subscribed_profiles]
                    
                    if not available_profiles:
                        break  # No more profiles to subscribe

                    subscription_profile = random.choice(available_profiles)  # Choose a random unsubscribed profile
                    SubscriptionFactory.create(user=subscription_profile, flexispace=flexispace)
                    subscribed_profiles.append(subscription_profile)
                # Create varying numbers of posts
                posts = [PostFactory.create(user=profile, flexispace=flexispace) for _ in range(random.randint(1, 3))]

                for post in posts:
                    contents = [ContentFactory.create(post=post) for _ in range(random.randint(1, 4))]

                    # Create varying numbers of comments
                    comments = [CommentFactory.create(user=profile, post=post) for _ in range(random.randint(1, 10))]

                    # Create votes for the post
                    post_vote_count = random.randint(1, 8)
                    for _ in range(post_vote_count):
                        VoteFactory.create(user=profile, post=post, comment=None)

                    # Create votes for each comment
                    for comment in comments:
                        comment_vote_count = random.randint(1, 8)
                        for _ in range(comment_vote_count):
                            VoteFactory.create(user=profile, post=None, comment=comment)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))

