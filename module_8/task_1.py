import sqlite3

conn = sqlite3.connect('sqlite3.db')
cur = conn.cursor()  # позволяет делать запросы в базу данных
# создали 2 таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS Students(id INT,
 name TEXT,
 surname TEXT,
 age INTEGER,
 city TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Courses(
   id INT,
   name TEXT, 
   time_start TEXT,
   time_end TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Student_courses(
   course_id INT,
   student_id INT);
""")
conn.commit()
# помещаю в таблицу Courses элементы
# courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
#
# cur.executemany("""INSERT INTO Courses(id, name, time_start, time_end)
#     VALUES(?, ?, ?, ?);""", courses)
# conn.commit()

# помещаю в таблицу Students элементы
# students = [(1, 'Max', 'Brooks', 24, 'Spb'),
#             (2, 'John', 'Stones', 15, 'Spb'),
#             (3, 'Andy', 'Wings', 45, 'Manhester'),
#             (4, 'Kate', 'Brooks', 34, 'Spb')]
# cur.executemany("""INSERT INTO Students(
#  id,
#  name,
#  surname,
#  age,
#  city) VALUES(?, ?, ?, ?, ?);""", students)
# conn.commit()

# помещаю в таблицу Student_courses элементы
# Keys = [(1, 1), (2, 1), (3, 1), (4, 2)]
# cur.executemany("""INSERT INTO Student_courses(student_id, course_id) VALUES(?, ?);""", Keys)
# conn.commit()

# вывели студентов старше 30
cur.execute("SELECT * FROM Students WHERE age>30;")
old_students = cur.fetchall()
print(old_students)

# всех студентов кто проходит курс python
cur.execute("""SELECT * FROM Student_courses JOIN Students ON Student_courses.student_id = Students.id WHERE course_id=1;""")
python_students = cur.fetchall()
print(python_students)

# Всех студентов, которые проходят курс по python и из Spb.

cur.execute("""SELECT Students.name FROM Student_courses JOIN Students ON Student_courses.student_id = Students.id WHERE Students.city = 'Spb' AND course_id = 1;""")
spb_python_students = cur.fetchall()
print(spb_python_students)