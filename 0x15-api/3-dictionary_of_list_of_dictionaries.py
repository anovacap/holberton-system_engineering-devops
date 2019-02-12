#!/usr/bin/python3
"""Using a REST API for returns all information about his / her TODO list
progress in json file"""
import json
import requests
import sys


def main():
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo = requests.get(todos_url)
    user = requests.get(user_url)
    todo_js = todo.json()
    user_js = user.json()
    file = "todo_all_employees.json"
    with open(file, 'w') as json_file:
        api_json = {}
        for x in user_js:
            task_l = []
            for y in todo_js:
                if y['userId'] == x['id']:
                    task_l.append({'username': x['username'],
                                   'task': y['title'],
                                   'completed': y['completed']})
            api_json[x['id']] = task_l
        json_file.write(json.dumps(api_json))

if __name__ == "__main__":
    main()
