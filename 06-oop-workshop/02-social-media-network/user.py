class User:
    def __init__(self, id_, name, age):
        self.id = id_
        self.name = name
        self.age = age
        self.friend_ids = []
        self.blocked_ids = []

    def add_friend(self, user_id):
        self.friend_ids.append(user_id)

    def block_user(self, user_id):
        self.blocked_ids.append(user_id)

    def is_user_blocked(self, user_id):
        for id_ in self.blocked_ids:
            if id_ == user_id:
                return True
        return False
