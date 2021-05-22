#!/usr/bin/python3
""" Module for storing the show_result method. """
from os import get_terminal_size
from sys import argv as av
from requests import get
from os import path
from time import sleep
from random import randint as rand

def show_result(correction_id='', task={}):
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

    good_emoji = ['🔥', '⚡', '✨', '🎊', '🎉', '🏆', '🏅', '⭐', '🥂']
    bad_emoji = ['🤢', '🤕', '🤮', '🥵', '🤒', '😵', '🤯', '🥶', '🩹']

    i = 1
    while response.json()['status'] != 'Done':
        print("Checking your code... {}".format(good_emoji[rand(0,8)]))
        sleep(0.2)
        print('▋▋' * i)
        if response.json()['status'] == 'Done':
            print("\033[K")
            break
        print("\033[1;0f")
        i += 1
        response = get(url)
    print('')

    for check in response.json()['result_display']['checks']:
        check_type = check['check_label']
        appproved = check['passed']
        title = check['title']
        if appproved:
            print('\033[92m', end = '')
            print("{} {}: Approved {}".format(good_emoji[rand(0,8)],
                                              title,
                                              good_emoji[rand(0,8)]))
            print('\033[m', end = '')
        else:
            print('\033[91m', end = '')
            print("{} {}: NOT Approved {}".format(bad_emoji[rand(0,8)],
                                                  title,
                                                  bad_emoji[rand(0,8)]))
            print('\033[m', end = '')
