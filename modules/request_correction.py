#!/usr/bin/python3
""" Module for printing the id of all tasks of current project. """
from sys import argv as av
from requests import post
from os import environ


def request_correction():
    """ Prints all of the ids of the tasks in the given project. """
    if len(av) != 2:
        print("usage...")
        exit()

    if path.exists('/tmp/.hbnb_auth_token') is None:
        print("No /tmp/.hbnb_auth_token file...")
        exit()

    with open('/tmp/.hbnb_auth_token', 'r') as f:
        auth = f.read()

    url = "https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}" \
    .format(av[1], auth)

    response = post(url, data='')

    request_result = response.json()

    print(request_result)

if __name__ == '__main__':
    request_correction()
