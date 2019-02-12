#!/usr/bin/python3
"""Using a REST API for a given employee ID, returns
information about his / her TODO list progress """
import requests
import sys


def main():
    if len(sys.argv) == 1:
        return
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo = requests.get(todos_url)
    user = requests.get(user_url)
    todo_js = todo.json()
    user_js = user.json()
    count_tasks = 0
    count_finished = 0
    tasks = []
    for x in user_js:
        if x.get('id') == int(sys.argv[1]):
            name = x.get('name')
    for y in todo_js:
        if y.get('userId') == int(sys.argv[1]):
            count_tasks += 1
            if y.get('completed') == bool('true'):
                count_finished += 1
                tasks.append(y.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          count_finished,
                                                          count_tasks))
    for z in tasks:
        print("\t{}".format(z))

if __name__ == "__main__":
    main()
