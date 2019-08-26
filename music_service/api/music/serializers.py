from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ['title', 'artist']
