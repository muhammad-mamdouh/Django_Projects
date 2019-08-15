from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import misaka
from subreddits.models import Subreddit


class Post(models.Model):
    message = models.TextField()
    message_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:100]

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
