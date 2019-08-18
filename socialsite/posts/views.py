from django.views.generic import ListView
from braces.views import SelectRelatedMixin
from .models import Post


class PostList(SelectRelatedMixin, ListView):
    model = Post
    select_related = ('user', 'subreddit')
