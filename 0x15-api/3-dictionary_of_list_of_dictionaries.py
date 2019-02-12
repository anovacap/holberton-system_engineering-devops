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
    task_l = []
    u_id = []
    uname = []
    for x in user_js:
        u_id.append(x.get('id'))
        uname.append(x.get('username'))
    for y in todo_js:
        if y.get('completed') is True:
            completed = 'true'
        if y.get('completed') is False:
            completed = 'false'
        tasks = y.get('title')
        for z in uname:
            task_d = {'task': tasks, 'completed': completed,
                      'username': z}
        task_l.append(task_d)
        for i in u_id:
            api_json = {i: task_l}
    with open(file, 'w') as json_file:
        json.dump(api_json, json_file)

if __name__ == "__main__":
    main()
