from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def get_approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=150)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return f'{self.text[0:100]} ...'
