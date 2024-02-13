import uuid


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex
        self.favorite_movies = []

    def add_favorite_movie(self, movie_id):
        self.favorite_movies.append(movie_id)
