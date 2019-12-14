import django_filters
from .models import Film

class FilmFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = {
            'title': ['icontains'],
            'duration': ['exact'],
            'price': ['gt', 'lt'],
        }
