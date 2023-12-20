#!/usr/bin/python3

"""This program gathers data from an API
"""

import requests
from sys import argv


def get_user_tasks(user_id):
    """Display TODO list progress for a given employee"""
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{api_url}users/{user_id}'
    todos_url = f'{api_url}users/{user_id}/todos'

    user_data = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    completed = [task for task in todos if task['completed']]

    name = user_data['name']
    completed_count = len(completed)
    total_count = len(todos)
    print(f"Employee {name} is done with tasks("
          f"{completed_count}/{total_count}):")

    for task in completed:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    get_user_tasks(int(argv[1]))
