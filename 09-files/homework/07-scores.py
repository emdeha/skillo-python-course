import csv
import json


def calculate_average(student_scores_with_subject):
    student_scores = [score for score in student_scores_with_subject.values()]
    return sum(student_scores) / len(student_scores)


def read_scores():
    exam_scores = {}

    with open('student_scores.csv') as scores:
        scores_reader = csv.reader(scores)
        scores_reader.__next__()

        for score in scores_reader:
            exam_scores[score[0]] = calculate_average(json.loads(score[1]))

    return exam_scores


def write_scores(exam_scores):
    with open('average_scores.json', 'w') as average_scores:
        json.dump(exam_scores, average_scores)


write_scores(read_scores())
