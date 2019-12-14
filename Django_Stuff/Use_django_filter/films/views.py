from django.shortcuts import render
from .models          import Film
from .filter          import FilmFilter


def film_list(request):
    films  = Film.objects.all()
    filter = FilmFilter(request.GET, queryset=films)

    return render(request, 'films/film_list.html', {'filter': filter})
