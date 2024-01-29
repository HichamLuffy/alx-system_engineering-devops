#!/usr/bin/python3
"""gather data from an API"""


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
    
    completed = [task.get("title") for task in todo if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for task in completed:
        print(f"\t{task}")
