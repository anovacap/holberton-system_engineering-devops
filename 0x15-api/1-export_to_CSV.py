#!/usr/bin/python3
"""Using a REST API for a given employee ID, returns
information about his / her TODO list progress """
import csv
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
        file = sys.argv[1] + ".csv"
        tasks = []
        status = []
        for x in user_js:
            if x.get('id') == int(sys.argv[1]):
                uname = x.get('username')
        for y in todo_js:
            if y.get('userId') == int(sys.argv[1]):
                if y.get('completed') == bool('true'):
                    status.append('True')
                else:
                    status.append('False')
                tasks.append(y.get('title'))
        combined = zip(status, tasks)
        with open(file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for i, z in combined:
                row = [sys.argv[1], uname, i, z]
                writer.writerow(row)

if __name__ == "__main__":
    main()
