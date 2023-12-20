#!/usr/bin/python3

"""This program gathers data from an API
"""
import json
import requests
from sys import argv


def export_tasks_to_json(user_id):
    """Export TODO list data for a given employee to a JSON file"""
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{api_url}users/{user_id}'
    todos_url = f'{api_url}users/{user_id}/todos'

    user_data = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    tasks_info = [
        {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_data['username']
        } for task in todos
    ]

    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump({str(user_id): tasks_info}, jsonfile)


if __name__ == '__main__':
    export_tasks_to_json(int(argv[1]))
