from typing import List

from .interface import RecommendationAlgorithm
from ..user import user
from ..movie import movie


class NoSuchMovieException(Exception):
    def __init__(self, message):
        super().__init__(message)


class DefaultAlgorithm(RecommendationAlgorithm):
    def run(self, _user: user.User, movies: List[movie.Movie]) -> List[movie.Movie]:
        return movies[0:3]


class AlgorithmByGenres(RecommendationAlgorithm):
    def run(self, _user: user.User, movies: List[movie.Movie]) -> List[movie.Movie]:
        first_movie = None
        for _movie in movies:
            if _movie.id == _user.favorite_movies[0]:
                first_movie = _movie

        if first_movie is None:
            raise NoSuchMovieException(f"Can't find movie {_user.favorite_movies[0]}")

        return list(filter(lambda m: m.genre == first_movie.genre, movies))
