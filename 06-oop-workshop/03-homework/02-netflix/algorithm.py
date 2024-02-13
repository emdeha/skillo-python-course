from abc import ABC, abstractmethod


class RecommendationAlgorithm(ABC):
    @abstractmethod
    def run(self, user, movies):
        pass


class DefaultAlgorithm(RecommendationAlgorithm):
    def run(self, _user, movies):
        return movies[0:3]


class AlgorithmByGenres(RecommendationAlgorithm):
    def run(self, user, movies):
        first_movie_genre = user.favorite_movies[0].genre
        return list(filter(lambda m: m.genre == first_movie_genre, movies))
