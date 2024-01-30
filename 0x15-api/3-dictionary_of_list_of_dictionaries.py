#!/usr/bin/python3
""" Export to CSV """


import json
import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API"""
    id_user = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    userid = f'users?id={id_user}'
    user_response = requests.get(f'{url}{userid}')
    user = user_response.json()
    todos = f'todos?userId={id_user}'
    done = f'{todos}&completed=true'
    todo_response = requests.get(f'{url}{todos}')
    todo = todo_response.json()
    Name = user[0].get("name")
    todosdone = requests.get(f'{url}{done}').json()
    todos_completed = len(todosdone)
    totaldone = len(todo)
    userName = user[0].get("username")

    with open(f"{id_user}.json", "w") as f:
        data = {
            id_user: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": userName,
                }
                for task in todos
            ]
        }
        json.dump(data, f)
