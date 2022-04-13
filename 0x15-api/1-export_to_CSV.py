#!/usr/bin/python3
"""getting data from an api and export in CSV
"""

import csv
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

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)

    for t in todos.json():
        if t.get("userId") == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as new_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})
