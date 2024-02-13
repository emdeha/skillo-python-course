from typing import Dict


class RatingManager:
    def __init__(self):
        self.__movie_ratings: Dict[str, float] = {}

    def rate_movie(self, movie_id: str, rating: float):
        self.__movie_ratings[movie_id] = rating

    def get_rating_for_movie(self, movie_id: str) -> float:
        return self.__movie_ratings[movie_id]
