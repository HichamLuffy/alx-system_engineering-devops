#!/usr/bin/python3
""" Export to CSV """


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

    csv_file = f'{id_user}.csv'
    with open(csv_file, 'w') as f:
       for task in todo:
           status = task.get("completed")
           if task.get("completed") is True:
               f.write("{}, {}, {}, {}\n".format(id_user, Name, status, task.get("title")))
