from django.shortcuts import render

from .models import Movie


# Create your views here.
def movies(request):
    movies_list = Movie.objects.all()
    context = {"movies": movies_list}
    return render(request, "movies.html", context)


def add_movie_form(request):
    return render(request, "add_movie.html")


def add(request):
    title = request.POST["title"]
    year = request.POST["year"]
    movie = Movie(title=title, publish_year=year)
    movie.save()
    return movies(request)
