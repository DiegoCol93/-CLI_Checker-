#!/usr/bin/python3
""" Module for printing the id of all tasks of current project. """
from sys import argv as av
from requests import get
from os import environ, path


def get_tasks(project_number):
    """ Prints all of the ids of the tasks in the given project. """

    if path.exists('/tmp/.hbnb_auth_token') is None:
        print("No /tmp/.hbnb_auth_token file...")
        return

    with open('/tmp/.hbnb_auth_token', 'r') as f:
        auth = f.read()

    url = "https://intranet.hbtn.io/projects/{}.json?auth_token={}" \
        .format(project_number, auth)

    response = get(url)

    try:
        tasks = response.json()['tasks']
    except Exception as e:
        print(e)
        return

    number = 0
    for task in tasks:
        print('{}. - {} id: '.format(number, task['title']), end='')
        print('{}'.format(task['id']))
        number += 1
