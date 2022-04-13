#!/usr/bin/python3
""" Script that get info using REST API """

import requests
from sys import argv

if __name__ == '__main__':
    endpoint = "https://https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(endpoint + "users/{}".
                         format(userId), verify=False).json()
    todo = requests.get(endpoint + "todos?userId={}".
                         format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as my_file:
        my_writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            my_writer.writerow([int(userId), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
