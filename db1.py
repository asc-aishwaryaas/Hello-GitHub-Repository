import sqlite3

#connect to the database
connection = sqlite3.connect("asc.db")

print("Database connected successfully")

#save the changes
connection.commit()

#close the connection
connection.close()