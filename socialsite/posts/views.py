from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.urls import reverse_lazy
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


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ('user', 'subreddit')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post has been deleted successfully!')
        return super().delete(*args, **kwargs)


class PostDetail(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ('user', 'subreddit')

    def get_queryset(self):
        queryset = super().queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
