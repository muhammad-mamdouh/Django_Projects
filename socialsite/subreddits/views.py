from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, RedirectView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Subreddit, SubredditMembers


class CreateSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddit
    fields = ['name', 'description']


class ListSubreddits(ListView):
    model = Subreddit


class JoinSubreddit(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('subreddits:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        subreddit = get_object_or_404(Subreddit, slug=self.kwargs.get('slug'))

        try:
            SubredditMembers.objects.create(user=self.request.user, subreddit=subreddit)
        except IntegrityError:
            messages.warning(self.request, 'Warning! Already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)


class LeaveSubreddit(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('subreddits:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = SubredditMembers.objects.filter(
                user = self.request.user,
                subreddit__slug=self.kwargs.get('slug')
            ).get()
        except SubredditMembers.DoesNotExist:
            messages.warning(self.request, "Sorry you aren't in this group!")
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')

        return super().get(request, *args, **kwargs)
