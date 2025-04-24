from django.contrib import admin
from .models import User, Community, subRabble, Post, Comment, Conversation, Message, Follow, PostLike, CommentLike

# Register your models here.
admin.site.register(User)
admin.site.register(Community)
admin.site.register(subRabble)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Follow)
admin.site.register(PostLike)
admin.site.register(CommentLike)
