from typing import Dict, List

from ..algorithm.implementation import DefaultAlgorithm, RecommendationAlgorithm
from ..movie.movie import Movie
from ..user.user import User


class Netflix:
    def __init__(self, algorithm: RecommendationAlgorithm = DefaultAlgorithm()):
        self.movies: Dict[str, Movie] = {}
        self.users: Dict[str, User] = {}
        self.algorithm = algorithm

    def add_movie(self, movie: Movie):
        self.movies[movie.id] = movie

    def remove_movie(self, movie_id: str):
        del self.movies[movie_id]

    def add_user(self, user: User):
        self.users[user.id] = user

    def change_recommendation_algorithm(self, recommendation_algorithm: RecommendationAlgorithm):
        self.algorithm = recommendation_algorithm

    def recommend_movies_to_user(self, user: User) -> List[Movie]:
        return self.algorithm.run(user, list(self.movies.values()))
