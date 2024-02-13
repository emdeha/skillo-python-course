from algorithm import DefaultAlgorithm


class Netflix:
    def __init__(self, algorithm=DefaultAlgorithm()):
        self.movies = {}
        self.users = {}
        self.algorithm = algorithm

    def add_movie(self, movie):
        self.movies[movie.id] = movie

    def remove_movie(self, movie_id):
        del self.movies[movie_id]

    def add_user(self, user):
        self.users[user.id] = user

    def change_recommendation_algorithm(self, recommendation_algorithm):
        self.algorithm = recommendation_algorithm

    def recommend_movies_to_user(self, user):
        return self.algorithm.run(user, list(self.movies.values()))
