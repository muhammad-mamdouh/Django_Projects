from django.db import models
from django.contrib.auth.models import User
from rest_framework.reverse import reverse as api_reverse


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user.username} posted about {self.title}'

    @property
    def owner(self):
        return self.user

    def get_api_url(self):
        return api_reverse('api-postings:post-rud', kwargs={'version': 'v1', 'pk': self.pk})
