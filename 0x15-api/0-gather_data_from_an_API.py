#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(api_url)
    EMPLOYEE_NAME = ""
    for i in users.json():
        if i.get("id") == int(argv[1]):
            EMPLOYEE_NAME = i.get("name")
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)

    for task in todos.json():
        if task.get("userId") == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS +=1
                TASK_TITLE.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
