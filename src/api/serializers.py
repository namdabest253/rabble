from rest_framework import serializers
from rabble.models import User, Community, subRabble, Post, Comment, Conversation, Message, Follow, PostLike, CommentLike

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_picture', 'bio', 'interests']
        
class subRabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = subRabble
        fields = ['id', 'community_id', 'identifier', 'title', 'description', 'privacy', 'anonymous', 'timestamp']

class PostSerializer(serializers.ModelSerializer):
    account_id = serializers.StringRelatedField()
    subRabble_id = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['id', 'account_id', 'subRabble_id', 'title', 'body', 'privacy', 'anonymous', 'timestamp']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['user', 'post']

