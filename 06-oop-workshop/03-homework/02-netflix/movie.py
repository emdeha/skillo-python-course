import uuid


class Movie:
    def __init__(self, title, genre, actors, source_file_name):
        self.title = title
        self.genre = genre
        self.actors = actors
        self.source_file_name = source_file_name
        self.id = uuid.uuid4().hex
