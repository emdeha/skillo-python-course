from abc import ABC, abstractmethod
from typing import List

from user import User
from movie import Movie


class NoSuchMovieException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RecommendationAlgorithm(ABC):
    @abstractmethod
    def run(self, user: User, movies: List[Movie]):
        pass


class DefaultAlgorithm(RecommendationAlgorithm):
    def run(self, _user: User, movies: List[Movie]) -> List[Movie]:
        return movies[0:3]


class AlgorithmByGenres(RecommendationAlgorithm):
    def run(self, user: User, movies: List[Movie]) -> List[Movie]:
        first_movie = None
        for movie in movies:
            if movie.id == user.favorite_movies[0]:
                first_movie = movie

        if first_movie is None:
            raise NoSuchMovieException(f"Can't find movie {user.favorite_movies[0]}")

        return list(filter(lambda m: m.genre == first_movie.genre, movies))
