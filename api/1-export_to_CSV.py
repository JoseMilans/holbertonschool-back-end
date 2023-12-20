#!/usr/bin/python3

"""This program gathers data from an API
"""
import csv
import requests
from sys import argv


def export_tasks_to_csv(user_id):
    """Export TODO list data for a given employee to a CSV file"""
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{api_url}users/{user_id}'
    todos_url = f'{api_url}users/{user_id}/todos'

    user_data = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csvwriter.writerow([user_id, user_data['username'],
                                task['completed'], task['title']])


if __name__ == '__main__':
    export_tasks_to_csv(int(argv[1]))
