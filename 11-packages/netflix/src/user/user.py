import uuid
from typing import List


class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex
        self.favorite_movies: List[str] = []

    def add_favorite_movie(self, movie_id: str):
        self.favorite_movies.append(movie_id)
