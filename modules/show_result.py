#!/usr/bin/python3
""" Module for storing the show_result method. """
from sys import argv as av
from requests import get
from os import path
from tqdm import tqdm


def show_result(correction_id='5028906'):
    """ Prints the result of the correction """

    if path.exists('/tmp/.hbnb_auth_token') is None:
        print("No /tmp/.hbnb_auth_token file...")
        return

    with open('/tmp/.hbnb_auth_token', 'r') as f:
        auth = f.read()

    url = 'https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}' \
        .format(correction_id, auth)

    response = get(url)

    for i in tqdm(range(10000)):
        pass
    print(response.json())


show_result()
