from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    commented_by_user = serializers.HyperlinkedRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        view_name='user-detail'
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("updated_at", "created_at")


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        view_name='user-detail'
    )
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("updated_at", "created_at", "author")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
