from django.urls import path

from . import views

urlpatterns = [
    path('', views.movies, name="movies"),
    path('add_form', views.add_movie_form, name="add_movie_form"),
    path('add', views.add, name="add")
]
