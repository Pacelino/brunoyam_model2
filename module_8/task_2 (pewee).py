from peewee import *

conn = SqliteDatabase('server.db')


class Students(Model):
    id = PrimaryKeyField(column_name='id', unique=True)

    name = TextField(column_name='name')

    surname = TextField(column_name='surname')

    age = IntegerField(column_name='age')

    city = TextField(column_name='city')

    class Meta:
        database = conn


class Courses(Model):
    id = PrimaryKeyField(column_name='id', unique=True)

    name = TextField(column_name='name')

    time_start = TextField(column_name='time_start')

    time_end = TextField(column_name='time_end')

    class Meta:
        database = conn


class Student_courses(Model):

    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)


    class Meta:
        database = conn


Students.create_table()
Student_courses.create_table()
Courses.create_table()
# добавили в таблицу Courses элементы
# courses1 = [
#     {'id': 1, 'name': 'python', 'time_start': '21.07.21', 'time_end': '21.08.21'},
#     {'id': 2, 'name': 'java', 'time_start': '13.07.21', 'time_end': '16.08.21'}
# ]
# Courses.insert_many(courses1).execute()
# добавили в таблицу Students элементы
# students = [
#     {'id': 1, 'name': 'Max', 'surname': 'Brooks', 'age': 24, 'city': 'Spb'},
#     {'id': 2, 'name': 'John', 'surname': 'Stones', 'age': 15, 'city': 'Spb'},
#     {'id': 3, 'name': 'Andy', 'surname': 'Wings', 'age': 45, 'city': 'Manhester'},
#     {'id': 4, 'name': 'Kate', 'surname': 'Brooks', 'age': 34, 'city': 'Spb'}
# ]
# Students.insert_many(students).execute()
# добавили в таблицу Students_courses элементы
# student_select = Students.select()
# course_select = Courses.select()
# student_corses = [
#     {'student_id': student_select[0], 'course_id': course_select[0]},
#     {'student_id': student_select[1], 'course_id': course_select[0]},
#     {'student_id': student_select[2], 'course_id': course_select[0]},
#     {'student_id': student_select[3], 'course_id': course_select[1]},
# ]
# Student_courses.insert_many(student_corses).execute()

# 1. Всех студентов старше 30 лет.
old_students = Students.select().where(Students.age > 30)
for i in old_students:
    print('student over 30: ',i.name)
# 2. Всех студентов, которые проходят курс по python.
python_student = Students.select().join(Student_courses).where(Student_courses.course_id == 1)
for k in python_student:
    print('student lern python: ', k.name)
# 3. Всех студентов, которые проходят курс по python и из Spb.
stundent_in_spb_and_lern_python = Students.select().join(Student_courses).where(Student_courses.course_id == 1, Students.city == 'Spb')
for n in stundent_in_spb_and_lern_python:
    print(n.name)