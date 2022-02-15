from rest_framework import serializers
from blog.models import Category, Post,Comment


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('id', 'slug', 'title', 'author','comments', 'excerpt', 'content', 'status','category')
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user_name')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']
