import csv


def input_students():
    students = {}

    number_of_students = int(input("How many students are there?"))

    for i in range(0, number_of_students):
        name = input("Name:")
        score = int(input("Score:"))
        students[name] = score

    return students


def write_to_csv(students):
    with open('students_scores_input.csv', 'w') as students_scores:
        writer = csv.writer(students_scores)

        for name, score in students.items():
            writer.writerow([name, score])


write_to_csv(input_students())
