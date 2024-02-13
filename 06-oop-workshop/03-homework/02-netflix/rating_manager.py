class RatingManager:
    def __init__(self):
        self.__movie_ratings = {}

    def rate_movie(self, movie_id, rating):
        self.__movie_ratings[movie_id] = rating

    def get_rating_for_movie(self, movie_id):
        return self.__movie_ratings[movie_id]
