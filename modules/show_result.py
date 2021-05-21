#!/usr/bin/python3
""" Module for storing the show_result method. """
from os import get_terminal_size
from sys import argv as av
from requests import get
from os import path
from time import sleep


def show_result(correction_id='5029461'):
    """ Prints the result of the correction """

    size = get_terminal_size()
    col = size.columns

    if path.exists('/tmp/.hbnb_auth_token') is None:
        print("No /tmp/.hbnb_auth_token file...")
        return

    with open('/tmp/.hbnb_auth_token', 'r') as f:
        auth = f.read()

    url = 'https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}' \
    .format(correction_id, auth)

    response = get(url)

    while response.json()['status'] != 'Done':
        sleep(0.5)
        i = 1
        for i in range(col):
            sleep(0.2)
            print('|' * i)
            # print("Checking your code... {}".format(char))
            print("\033[1;0f")
            i += 1
        response = get(url)

    for check in response.json()['result_display']['checks']:
        check_type = check['check_label']
        appproved = check['passed']
        title = check['title']
        print("{}: Approved: {} Type: {}".format(check['title'],check['passed'],check['check_label']))
