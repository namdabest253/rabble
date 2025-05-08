from factory import Sequence, Faker, SubFactory
from factory.django import DjangoModelFactory
from django.utils.timezone import now
from ..models import User, Community, subRabble, Post, Comment

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    password = 'password123'

class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Community
    community_identifier = Sequence(lambda n: f"community{n}")
    owner_id = SubFactory(UserFactory)
    timestamp = now()

class SubRabbleFactory(DjangoModelFactory):
    class Meta:
        model = subRabble
    community_id = SubFactory(CommunityFactory)
    identifier = Sequence(lambda n: f"subrabble{n}")
    title = Faker("sentence")
    description = Faker("paragraph")
    privacy = False
    anonymous = False
    timestamp = now()

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    account_id = SubFactory(UserFactory)
    subRabble_id = SubFactory(SubRabbleFactory)
    title = Faker("sentence")
    body = Faker("paragraph")
    privacy = False
    anonymous = False
    timestamp = now()

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    account_id = SubFactory(UserFactory)
    post_id = SubFactory(PostFactory)
    body = Faker("text")
    anonymous = False
    parent_comment_id = None
    timestamp = now()
