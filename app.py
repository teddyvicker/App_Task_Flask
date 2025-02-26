from flask import Flask, request
from models.tasks import Task


app = Flask(__name__)


# CRUD
# Creat, read, Update and Delete
# Tabela : Tarefa 
tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Test'

if __name__ == "__main__":
    app.run(debug=True)