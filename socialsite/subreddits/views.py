from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Subreddit


class CreateSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddit
    fields = ['name', 'description']
