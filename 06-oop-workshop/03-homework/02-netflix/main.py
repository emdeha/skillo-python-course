from netflix import Netflix
from movie import Movie
from user import User
from algorithm import AlgorithmByGenres, DefaultAlgorithm
from rating_manager import RatingManager

netflix = Netflix(AlgorithmByGenres())

# TODO: Add rating
movie = Movie(title="Time Keepers", genre="comedy", actors=[], source_file_name="")
movie_two = Movie(title="James Bond", genre="action", actors=[], source_file_name="")
movie_three = Movie(title="Baywatch", genre="comedy", actors=[], source_file_name="")

user = User(email="a@a.com", password="asdf123")

rating_manager = RatingManager()

netflix.add_movie(movie)
netflix.add_movie(movie_two)
netflix.add_movie(movie_three)

netflix.add_user(user)

user.add_favorite_movie(movie_three)

recommended_movies = netflix.recommend_movies_to_user(user)

netflix.change_recommendation_algorithm(DefaultAlgorithm())

recommended_movies_two = netflix.recommend_movies_to_user(user)

rating_manager.rate_movie(movie.id, 5)

rating = rating_manager.get_rating_for_movie(movie.id)

print("end")
