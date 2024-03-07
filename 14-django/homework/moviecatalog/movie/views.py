from django.views.generic.list import ListView
from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
