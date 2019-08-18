from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from .models import Post


class PostList(SelectRelatedMixin, ListView):
    model = Post
    select_related = ('user', 'subreddit')


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = Post
    select_related = ('user', 'subreddit')
    fields = ['message', 'subreddit']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
