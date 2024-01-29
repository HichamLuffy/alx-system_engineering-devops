#!/usr/bin/python3
""" gather data from an API """


import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API """
    id_user = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(url + f'users/{id_user}')
    user = user_response.json()
    todo_response = requests.get(url + f'todos?userId={id_user}')
    todo = todo_response.json()

    completed_tasks = [task['title'] for task in todo if task['completed']]
    print(
        f"Employee {user['name']} is done\
          with tasks({len(completed_tasks)}/{len(todo)}):")
    for task in completed_tasks:
        print(f"\t{task}")
