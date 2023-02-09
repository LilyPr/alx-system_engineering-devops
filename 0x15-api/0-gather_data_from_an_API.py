#!/usr/bin/python3
""" Uses JSONPlaceholder API to get information about emplif __name__ == "__main__":
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
        Re = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                         .format(argv[1])).json()
        Re_two = requests.get(
                'https://jsonplaceholder.typicode.com/todos/?userId={:}'
                .format(argv[1])).json()

        EMPLOYEE_NAME = Re.get('name')
        TASK_TITLE = []
        NUMBER_OF_DONE_TASKS = 0

        for task in Re_two:
                if task.get('completed') is True:
                        TASK_TITLE.append(task.get('title'))
                        NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(Re_two)
        print("Employee {} is done with tasks({}/{}):".
              format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                     TOTAL_NUMBER_OF_TASKS))

        for t in TASK_TITLE:
                print("\t {}".format(t))
