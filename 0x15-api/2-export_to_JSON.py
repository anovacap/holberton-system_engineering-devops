#!/usr/bin/python3
"""Using a REST API for a given employee ID, returns
information about his / her TODO list progress """
import json
import requests
import sys


def main():
    if len(sys.argv) == 2 and type(eval(sys.argv[1])) == int:
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        user_url = "https://jsonplaceholder.typicode.com/users"
        todo = requests.get(todos_url)
        user = requests.get(user_url)
        todo_js = todo.json()
        user_js = user.json()
        file = sys.argv[1] + ".json"
        task_l = []
        for x in user_js:
            if x.get('id') == int(sys.argv[1]):
                uname = x.get('username')
        for y in todo_js:
            if y.get('userId') == int(sys.argv[1]):
                if y.get('completed') is True:
                    completed = 'true'
                if y.get('completed') is False:
                    completed = 'false'
                tasks = y.get('title')
                task_d = {'task': tasks, 'completed': completed,
                          'username': uname}
                task_l.append(task_d)
        api_json = {sys.argv[1]: task_l}
        with open(file, 'w') as json_file:
            json.dump(api_json, json_file)

if __name__ == "__main__":
    main()
