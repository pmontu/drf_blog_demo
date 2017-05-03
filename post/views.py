from rest_framework import viewsets, mixins
from .serializers import (
    PostSerializer, CommentSerializer, UserSerializer
)
from .models import Post, Comment
from django.contrib.auth.models import User


class PostViewSet(
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
        ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(
            mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,
            viewsets.GenericViewSet
        ):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
        ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
