from user import User
from exceptions import InvalidArgument


class SocialMediaNetwork:
    def __init__(self):
        self.users = []
        self.messages = []  # {sender, receiver, message}

    def show_friends_for_user(self, user):
        if not isinstance(user, User):
            raise InvalidArgument("user must be User")

        friends = []
        for u in self.users:
            for friend in user.friend_ids:
                if u.id == friend:
                    friends.append(u)
        return friends

    def send_message(self, sender_id, receiver_id, message):
        if not isinstance(sender_id, int):
            raise InvalidArgument("sender_id must be int")
        if not isinstance(receiver_id, int):
            raise InvalidArgument("receiver_id must be int")
        if not isinstance(message, str):
            raise InvalidArgument("message must be str")

        self.messages.append({
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "message": message
        })

    def read_messages_for_user(self, user_id):
        if not isinstance(user_id, int):
            raise InvalidArgument("user_id must be int")

        messages_for_user = []
        for message in self.messages:
            if message.receiver_id == user_id and \
                    not user.is_user_blocked(message.sender_id):
                messages_for_user.append(message)
        return messages_for_user


social_media_network = SocialMediaNetwork()

user = User(1, "T", 29)

user.add_friend(2)
user.block_user(3)

social_media_network.send_message(sender_id=1, receiver_id=2, message="T")
messages = social_media_network.read_messages_for_user(user_id=1)

user.create_post(text)

feed = user.browse_news_feed()

social_media_network.show_friends_for_user(user)
