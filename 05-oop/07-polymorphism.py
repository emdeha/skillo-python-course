class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # This method will be overridden in subclasses


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows!"


class Duck(Animal):
    def make_sound(self):
        return f"{self.name} quacks!"


class Person:
    def speak(self):
        return "I speak"


def make_all_animals_sound(animals):
    for animal in animals:
        print(animal.make_sound())


make_all_animals_sound([Dog("Buddy"), Cat("Whiskers"), Duck("Daffy")])
