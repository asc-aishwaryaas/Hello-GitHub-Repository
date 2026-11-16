from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():

    students = [
        {
            "id":1,
            "name":"Rahul"
        },
        {
            "id":2,
            "name":"Anjali"
        }
    ]

    return jsonify(students)



app.run(debug=True)
print(a)
