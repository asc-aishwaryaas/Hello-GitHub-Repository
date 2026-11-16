from flask import Flask, request, jsonify
 
app = Flask(__name__)
students = []
 
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)
 
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify(data), 201
 
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    students[id] = request.get_json()
    return jsonify(students[id])
 
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    students.pop(id)
    return '', 204
 
if __name__ == '__main__':
    app.run(debug=True)