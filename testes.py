import pytest
import requests

#CRUD

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_creat_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200 
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def teste_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def teste_update_task():
    if tasks:
        tasks_id = tasks[0]
        payload = {
            "completed": True, 
            "description": "Nova Requisição",
            "title": "Título atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{tasks_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        
        #Nova Requisição
        response = requests.get(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload ["title"]
        assert response_json["description"] == payload ["description"]
        assert response_json["completed"] == payload ["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
        
        #response_json = response_json()
        #assert task_id == response_json['id']
        