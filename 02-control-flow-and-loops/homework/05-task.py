import random

problem = "Guess the number: "
expected = random.randrange(1, 100)

actual = int(input(problem))
while actual != expected:
    if actual > expected:
        print("Too low!")
    elif actual < expected:
        print("Too high!")

    actual = int(input(problem))

print("You guessed right!")
