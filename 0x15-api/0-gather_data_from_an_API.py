#!/usr/bin/python3
# gather data from an API


import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API """
    try:
        id_user = sys.argv[1]
        url = f'https://jsonplaceholder.typicode.com/'
        user_response = requests.get(url + f'users/{id_user}')
        user = user_response.json()
        todo_response = requests.get(url + f'todos?userId={id_user}')
        todo = todo_response.json()

        completed_tasks = [task['title'] for task in todo if task['completed']]
        print(
            f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(todo)}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except IndexError:
        print("Error: Please provide an employee ID as a command line argument.")
    except ValueError:
        print("Error: Employee ID should be an integer.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
