from django.db import models
from django.contrib.auth.models import AbstractUser
from django .utils import timezone

class User(AbstractUser):
    # user_id = models.IntegerField(primary_key=True)
    profile_picture = models.ImageField(blank=True, null=False)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    # timestamp = models.DateTimeField(default=timezone.now)

class Community(models.Model):
    # community_id = models.IntegerField(primary_key=True)
    community_identifier = models.TextField(unique=True)
    user_id = models.ManyToManyField(User, blank=True, null=True, related_name="community_users")
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "community_owner")
    admin_id = models.ManyToManyField(User, related_name = "community_admins")
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.community_identifier

class subRabble(models.Model):
    # subRabble_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="rubRabbles")
    identifier = models.TextField(unique=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    privacy = models.BooleanField()
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.identifier

class Post(models.Model):
    # post_id = models.IntegerField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    subRabble_id = models.ForeignKey(subRabble, on_delete=models.CASCADE, related_name="posts")
    title = models.TextField()
    body = models.TextField()
    privacy = models.BooleanField()
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):
    # comment_id = models.IntegerField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent_comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    body = models.TextField()
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body

class Conversation(models.Model):
    # conversation_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="conversations")
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations")
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    # message_id = models.IntegerField(primary_key=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Follow(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "following")
    followed_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followers")
    timestamp = models.DateTimeField(default=timezone.now)

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comments")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user", "comment")

    def __str__(self):
        return f"{self.user.username} liked comment {self.comment.pk}"