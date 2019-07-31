from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    body = models.TextField()
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def date_published_formatted(self):
        return f'{self.date_published.strftime("%b %-d, %Y")}'

    def summary(self):
        return f'{self.body[:250]} ...'
