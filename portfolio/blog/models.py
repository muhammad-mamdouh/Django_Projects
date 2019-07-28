from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title} Blog'

    def summary(self):
        return f'{self.body[:250]} ...'
