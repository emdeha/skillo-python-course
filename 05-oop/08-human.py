import json


class Human:
    def __init__(self, height, weight, nationality):
        self.height = height
        self.weight = weight
        self.nationality = nationality

    def __str__(self):
        return "Human:\n" + \
            f"Weight: {self.weight}\n" + \
            f"Height: {self.height}\n" + \
            f"Nationality: {self.nationality}\n" + \
            f"Gender: {self.gender()}\n"

    def __repr__(self):
        return json.dumps({
            "weight": self.weight,
            "height": self.height,
            "nationality": self.nationality,
            "gender": self.gender()
        })

    def __eq__(self, other):
        return self.weight == other.weight and \
            self.height == other.height and \
            self.nationality == other.nationality and \
            self.gender() == other.gender()

    def __lt__(self, other):
        return True

    def __len__(self):
        return self.height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def gender(self):
        pass


class Man(Human):
    def gender(self):
        return 'Male'


class Woman(Human):
    def gender(self):
        return 'Female'


man = Man(180, 80, 'Bulgarian')
woman = Woman(155, 45, 'Bulgarian')
man_two = Man(180, 80, 'Bulgarian')

print(man)
print(woman)

print("man == woman?", man == woman)
print("man == man?", man == man)
print("man == man_two?", man == man_two)

print(repr(man))

print("Height:", len(man))

print("man < woman?", man < woman)
