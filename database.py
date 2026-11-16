import sqlite3

#connect to the database
connection = sqlite3.connect("meow.db")

print("Database connected successfully")

#create a cursor
cursor = connection.cursor()

#create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
course TEXT
)
""")

''' example for inserting records using execute() statements
cursor.execute(""" INSERT INTO students(id, name, course) VALUES(1, 'Aishwarya','BCA')""")
'''

''' example for inserting records using multiple execute() statements
cursor.execute(""" INSERT INTO students(id, name, course) VALUES(1, 'Aishwarya','BCA')""")
cursor.execute(""" INSERT INTO students(id, name, course) VALUES(2, 'Manjushree','BBA')""")
cursor.execute(""" INSERT INTO students(id, name, course) VALUES(3, 'Sumitra','BCom')""")
'''

#example for inserting records using executemany()
students = [
    (11, "Rahul", "BSc"),
    (12, "Kishor", "MSc"),
    (13, "Sanjay", "MBA")
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students)

cursor.execute("SELECT * FROM students")
#rows = cursor.fetchall()
rows = cursor.fetchone()

print(rows)

#save the changes
connection.commit()

#close the connection
connection.close()