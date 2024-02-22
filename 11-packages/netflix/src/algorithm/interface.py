from abc import ABC, abstractmethod
from typing import List

from ..user import user
from ..movie import movie


class RecommendationAlgorithm(ABC):
    @abstractmethod
    def run(self, _user: user.User, movies: List[movie.Movie]):
        pass
