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
        title = task['title']
        task_id = task['id']
        print('{}. - {} id: '.format(number, title), end='')
        print('{}'.format(task_id))
        tasks_dict[str(number)] = [title, task_id]
        number += 1

    with open('/.current_project', 'w') as f:
        json.dump(tasks_dict, f)


    return(tasks_dict)
