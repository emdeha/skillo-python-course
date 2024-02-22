import uuid
from typing import List


class Movie:
    def __init__(self, title: str, genre: str, actors: List[str], source_file_name: str):
        self.title = title
        self.genre = genre
        self.actors = actors
        self.source_file_name = source_file_name
        self.id = uuid.uuid4().hex
