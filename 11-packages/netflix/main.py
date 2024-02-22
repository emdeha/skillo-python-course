from src.core.netflix import Netflix
from src.movie.movie import Movie
from src.user.user import User
from src.algorithm.implementation import AlgorithmByGenres

netflix = Netflix(AlgorithmByGenres())

movie = Movie(title="Time Keepers", genre="comedy", actors=[], source_file_name="")
movie_two = Movie(title="James Bond", genre="action", actors=[], source_file_name="")
movie_three = Movie(title="Baywatch", genre="comedy", actors=[], source_file_name="")

user = User(email="a@a.com", password="asdf123")

netflix.add_movie(movie)
netflix.add_movie(movie_two)
netflix.add_movie(movie_three)

netflix.add_user(user)
