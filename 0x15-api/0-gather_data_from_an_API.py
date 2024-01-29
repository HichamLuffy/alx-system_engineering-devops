#!/usr/bin/python3
# gather data from an API


import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API """
    id_user = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(id_user)).json()
    todo = requests.get(url + "todos?userId={}".format(id_user)).json()

    completed = [task.get("title") for task in todo if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for task in completed:
        print(f"\t{task}")
