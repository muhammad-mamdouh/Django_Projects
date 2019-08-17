from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Subreddit


class CreateSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddit
    fields = ['name', 'description']


class ListSubreddits(ListView):
    model = Subreddit
