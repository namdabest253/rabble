from django.db import models
from django.contrib.auth.models import AbstractUser
from django .utils import timezone

class User(AbstractUser):
    # user_id = models.IntegerField(primary_key=True)
    profile_picture = models.ImageField(blank=True, null=False)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

class Community(models.Model):
    # community_id = models.IntegerField(primary_key=True)
    community_identifier = models.TextField(unique=True)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="community_users")
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "community_owner")
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "community_admin")
    timestamp = models.DateTimeField(default=timezone.now)

class subRabble(models.Model):
    # subRabble_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    descriptive_name = models.TextField()
    description = models.TextField(blank=True, null=True)
    privacy = models.BooleanField()
    annonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)

class Post(models.Model):
    # post_id = models.IntegerField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subRabble_id = models.ForeignKey(subRabble, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    privacy = models.BooleanField()
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    # comment_id = models.IntegerField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)

class Conversation(models.Model):
    # conversation_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    # message_id = models.IntegerField(primary_key=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Follow(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "following")
    followed_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followers")
    timestamp = models.DateTimeField(default=timezone.now)