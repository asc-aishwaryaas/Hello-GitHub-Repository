from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():

    connection = sqlite3.connect("meow.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    connection.close()

    return str(rows)

app.run(debug=True)