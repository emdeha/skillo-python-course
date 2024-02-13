from exceptions import InvalidArgument


class User:
    def __init__(self, id_, name, age):
        if not isinstance(id_, int):
            raise InvalidArgument("id_ must be int")
        if not isinstance(name, str):
            raise InvalidArgument("name must be str")
        if not isinstance(age, int):
            raise InvalidArgument("age must be int")

        self.id = id_
        self.name = name
        self.age = age
        self.friend_ids = []
        self.blocked_ids = []

    def add_friend(self, user_id):
        if not isinstance(user_id, int):
            raise InvalidArgument("user_id must be int")

        self.friend_ids.append(user_id)

    def block_user(self, user_id):
        if not isinstance(user_id, int):
            raise InvalidArgument("user_id must be int")

        self.blocked_ids.append(user_id)

    def is_user_blocked(self, user_id):
        if not isinstance(user_id, int):
            raise InvalidArgument("user_id must be int")

        for id_ in self.blocked_ids:
            if id_ == user_id:
                return True
        return False
