import random

problems_and_answers = {
    "How much is 5 + 17? ": 22,
    "How much is 5 + 20? ": 25,
    "How much is 10 + 17? ": 27
}

problems = list(problems_and_answers.keys())
chosen_problem = problems[
    random.randint(0, len(problems_and_answers))
]

answer = problems_and_answers[chosen_problem]
while answer != int(input(chosen_problem)):
    print("Wrong guess! Try again!")

print("You guessed right!")
