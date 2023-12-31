from flask import Flask,jsonify
from flask import request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description for Task 1", "due_date": "12-01-2025", "status": "Complete"},
    {"id": 2, "title": "Task 2", "description": "Description for Task 2","due_date": "13-05-2025", "status": "Incomplete"},
]

@app.route('/details', methods=['GET'])
def details():
    return jsonify(tasks)

@app.route('/create', methods = ['POST'])
def task():
    if not request.json:
        return jsonify({'message': 'Invalid request. No JSON data provided.'}), 400

    title = request.json.get('title')
    description = request.json.get('description')
    due_date = request.json.get("due_date")
    status = request.json.get("status")

    if not title or not description:
        return jsonify({'message': 'Invalid request. Missing title or description.'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': status,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.json['title']
        task['description'] = request.json['description']
        task['due_date'] = request.json['due_date']
        task['status'] = request.json['status']
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found.'}), 404

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted.'})
    else:
        return jsonify({'message': 'Task not found.'}), 404
    return

if __name__=="__main__":
    app.run(debug=True)
