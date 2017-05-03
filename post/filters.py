import django_filters
from .models import Post


class PostFilter(django_filters.rest_framework.FilterSet):
    author_id = django_filters.NumberFilter(name="author__id")

    class Meta:
        model = Post
        fields = ['author', ]
