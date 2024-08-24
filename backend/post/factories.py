import factory
from faker import Faker
from user.models import Profile
from flexispace.models import FlexiSpace
from .models import Post, Content, Comment, Vote
from user.factories import ProfileFactory

fake = Faker()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'Post Title {n}')
    user = factory.SubFactory('your_app.factories.ProfileFactory')  # Assuming you have ProfileFactory
    flexispace = factory.SubFactory('your_app.factories.FlexiSpaceFactory')  # Assuming you have FlexiSpaceFactory
    upvotes = factory.LazyFunction(lambda: fake.random_int(min=0, max=100))
    downvotes = factory.LazyFunction(lambda: fake.random_int(min=0, max=100))
    created_at = factory.LazyFunction(fake.date_time_this_year)
    updated_at = factory.LazyFunction(fake.date_time_this_year)


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Content

    post = factory.SubFactory(PostFactory)
    block_type = factory.Iterator(['text', 'image'])
    content_text = factory.LazyAttribute(lambda obj: fake.paragraph() if obj.block_type == 'text' else '')
    
    image_url = factory.Maybe(
        factory.LazyAttribute(lambda obj: obj.block_type == 'image'),
        yes_declaration=factory.django.ImageField(filename='default.jpg'),
        no_declaration=''
    )
    
    block_order = factory.Sequence(lambda n: n + 1)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    user = factory.SubFactory('your_app.factories.ProfileFactory')
    post = factory.SubFactory(PostFactory)
    parent_comment = None
    upvotes = factory.LazyFunction(lambda: fake.random_int(min=0, max=50))
    downvotes = factory.LazyFunction(lambda: fake.random_int(min=0, max=50))
    created_at = factory.LazyFunction(fake.date_time_this_year)
    updated_at = factory.LazyFunction(fake.date_time_this_year)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vote

    user = factory.SubFactory(ProfileFactory)
    vote_type = factory.Iterator([True, False])  # True for Upvote, False for Downvote
    created_at = factory.LazyFunction(fake.date_time_this_year)
    updated_at = factory.LazyFunction(fake.date_time_this_year)

    @factory.lazy_attribute
    def post(self):
        return self._post if hasattr(self, '_post') else None

    @factory.lazy_attribute
    def comment(self):
        return self._comment if hasattr(self, '_comment') else None

    @factory.post_generation
    def ensure_single_field(self, create, extracted, **kwargs):
        # Ensure only one of post or comment is set
        if self.post and self.comment:
            raise ValueError('Cannot specify both post and comment.')

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        post = kwargs.pop('post', None)
        comment = kwargs.pop('comment', None)

        if post and comment:
            raise ValueError('Cannot specify both post and comment.')
        
        if post:
            kwargs['post'] = post
        elif comment:
            kwargs['comment'] = comment

        return super()._create(model_class, *args, **kwargs)