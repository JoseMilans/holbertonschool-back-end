#!/usr/bin/python3

"""This program gathers data from an API
"""
import json
import requests


def export_all_tasks_to_json():
    """Export TODO list data for all employees to a JSON file"""

    api_url = 'https://jsonplaceholder.typicode.com/'
    users_data = requests.get(f'{api_url}users').json()
    todos_data = requests.get(f'{api_url}todos').json()

    all_tasks = {}
    for user in users_data:
        user_tasks = [
            {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            for task in todos_data if task['userId'] == user['id']
        ]
        all_tasks[user['id']] = user_tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == '__main__':
    export_all_tasks_to_json()
