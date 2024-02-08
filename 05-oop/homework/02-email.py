class Email:
    def __init__(self, user, domain):
        self.user = user
        self.domain = domain

    def __eq__(self, other):
        return self.user == other.user and \
            self.domain == self.domain

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.user}@{self.domain}"


email_one = Email("tsvetan", "gmail.com")
email_two = Email("alabala", "abv.bg")

print(email_one)
print(email_two)

print(email_one == email_two)
print(email_one != email_two)
