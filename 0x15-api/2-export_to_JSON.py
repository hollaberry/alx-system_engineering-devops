#!/usr/bin/python3
"""getting data from an api and export in JSON
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(api_url)
    for i in users.json():
        if i.get("id") == int(argv[1]):
            USERNAME = i.get("username")
            break
    TASK_STATUS_TITLE = []

    todos_url = "http://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)

    for t in todos.json():
        if t.get("userId") == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to json"""
    t = []
    for task in TASK_STATUS_TITLE:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)
