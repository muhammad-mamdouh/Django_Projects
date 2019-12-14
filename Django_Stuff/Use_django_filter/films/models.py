from django.db import models


class Film(models.Model):
    title       = models.CharField(max_length=225)
    description = models.TextField()
    duration    = models.IntegerField()
    price       = models.DecimalField(max_digits=4, decimal_places=2)
