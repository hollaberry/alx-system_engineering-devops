#!/usr/bin/python3
"""
extend Python script to export data in the JSON format
"""

import json
import requests

if __name__ == '__main__':
    USERS = []
    users_api = requests.get("https://jsonplaceholder.typicode.com/users")
    for i in users_api.json():
        USERS.append((i.get('id'), i.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """export to json"""
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)
