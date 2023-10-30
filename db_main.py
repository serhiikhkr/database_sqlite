import sqlite3

from creat_data import creating_data


N_STUDENTS = 40
N_GROUPS = 3
N_TEACHERS = 4
N_SUBJECTS = 6


def insert_data(student, teacher, subject, group, grade):
    try:
        with sqlite3.connect('db_sqlite') as conn:
            cur = conn.cursor()

            sql_to_students = """INSERT INTO students(student_name, group_id)
                                   VALUES (?, ?)"""
            cur.executemany(sql_to_students, student)

            sql_to_teachers = """INSERT INTO teachers(teacher_name)
                                   VALUES (?)"""
            cur.executemany(sql_to_teachers, teacher)

            sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                                  VALUES (?, ?)"""
            cur.executemany(sql_to_subjects, subject)

            sql_to_groups = """INSERT INTO groups(group_name)
                                  VALUES (?)"""
            cur.executemany(sql_to_groups, group)

            sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_received)
                                  VALUES (?, ?, ?, ?)"""
            cur.executemany(sql_to_grades, grade)

            conn.commit()
    except Exception as err:
        print(f'Ошибка заполнения таблиц {err}')
        conn.rollback()


if __name__ == '__main__':
    students, teachers, subjects, groups, grades = creating_data(N_STUDENTS, N_TEACHERS, N_SUBJECTS)
    insert_data(students, teachers, subjects, groups, grades)
