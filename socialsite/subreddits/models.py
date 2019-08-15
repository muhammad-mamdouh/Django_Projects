from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django import template
import misaka

register = template.Library()


class Subreddit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    members = models.ManyToManyField(User, through='SubredditMembers')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('subreddits:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class SubredditMembers(models.Model):
    subreddit = models.ForeignKey(Subreddit, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_subreddits', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('subreddit', 'user')
