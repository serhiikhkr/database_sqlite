from faker import Faker
import random

Faker.seed(0)

NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 4
NUMBER_SUBJECTS = 6

faker = Faker()


def creating_data(number_student, number_teachers, number_subjects):
    names_students = [(faker.name(), random.randint(1, 3)) for _ in range(number_student)]
    names_teachers = [(faker.name(),) for _ in range(number_teachers)]
    subjects = [(faker.job(), random.randint(1, 4)) for _ in range(number_subjects)]
    groups = [('A',), ('B',), ('C',)]
    grades = []

    for s in range(1, number_student + 1):
        for n_s in range(1, number_subjects + 1):
            for i in range(12):
                grades.append((s, n_s, random.randint(3, 5), faker.date()))

    return names_students, names_teachers, subjects, groups, grades


if __name__ == '__main__':
    a, b, c, d, e = creating_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
