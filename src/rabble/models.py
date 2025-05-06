from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django .utils import timezone

class User(AbstractUser):
    profile_picture = models.ImageField(blank=True, null=False)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Community(models.Model):
    community_identifier = models.TextField(unique=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "community_owner")
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.community_identifier

class subRabble(models.Model):
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
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent_comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    body = models.TextField()
    anonymous = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body

class Conversation(models.Model):
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="conversations")
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations")
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class Message(models.Model):
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

class CommunityAdminship(models.Model):
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_admins")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_communities")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id.username} is admin of {self.community_id.community_identifier}"
    class Meta:
        unique_together = ("community_id", "user_id")
        verbose_name = "Community Admin"
        verbose_name_plural = "Community Admins"

class CommunityAccount(models.Model):
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_accounts")
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account_communities")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account_id.username} is a member of {self.community_id.community_identifier}"
    class Meta:
        unique_together = ("community_id", "account_id")
        verbose_name = "Community Account"
        verbose_name_plural = "Community Accounts"

class CommunitySubRabble(models.Model):
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_subRabbles")
    subRabble_id = models.ForeignKey(subRabble, on_delete=models.CASCADE, related_name="subRabble_communities")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.subRabble_id.identifier} is in {self.community_id.community_identifier}"
    class Meta:
        unique_together = ("community_id", "subRabble_id")
        verbose_name = "Community SubRabble"
        verbose_name_plural = "Community SubRabbles"

class ConversationAccount(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="conversation_accounts")
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account_conversations")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account_id.username} is in conversation {self.conversation_id.pk}"
    class Meta:
        unique_together = ("conversation_id", "account_id")
        verbose_name = "Conversation Account"
        verbose_name_plural = "Conversation Accounts"
