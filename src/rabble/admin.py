from django.contrib import admin
from .models import User, Community, subRabble, Post, Comment, Conversation, Message, Follow, PostLike, CommentLike, CommunityAdminship, CommunityAccount, CommunitySubRabble, ConversationAccount

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_identifier', 'timestamp')

@admin.register(subRabble)
class SubRabbleAdmin(admin.ModelAdmin):
    list_display = ('id', 'identifier', 'title', 'community_id')
    search_fields = ('identifier', 'title')
    list_filter = ('privacy',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'account_id', 'subRabble_id', 'timestamp')
    search_fields = ('title', 'body')
    list_filter = ('privacy', 'anonymous')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'account_id', 'timestamp')
    search_fields = ('body',)
    list_filter = ('anonymous',)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation_id', 'sender_id', 'timestamp')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower_id', 'followed_id')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'timestamp')


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'timestamp')

@admin.register(CommunityAdminship)
class CommunityAdminshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_id', 'user_id', 'timestamp')

@admin.register(CommunityAccount)
class CommunityAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_id', 'account_id', 'timestamp')

@admin.register(CommunitySubRabble)
class CommunitySubRabbleAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_id', 'subRabble_id', 'timestamp')

@admin.register(ConversationAccount)
class ConversationAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation_id', 'account_id', 'timestamp')