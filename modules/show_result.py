#!/usr/bin/python3
""" Module for storing the show_result method. """
from sys import argv as av
from requests import get
from os import path


def show_result():
    """ Prints the result of the correction """

    if len(av) != 2:
        print("usage...")
        exit()

    if path.exists('/tmp/.hbnb_auth_token') is None:
        print("No /tmp/.hbnb_auth_token file...")
        exit()

    with open('/tmp/.hbnb_auth_token', 'r') as f:
        auth = f.read()

    url = 'https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}' \
    .format(av[1], auth)

    response = get(url)

    print(response.json())

if __name__ == '__main__':
    show_result()
