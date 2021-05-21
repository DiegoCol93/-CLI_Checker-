#!/usr/bin/python3
""" Module for storing the get_auth method. """
from os import environ, path
from sys import argv as av
from requests import post


def get_auth():
    """ Gets the authentication token for the current user. """
    # If wrong number of arguments were passed print usage.
    if len(av) != 4:
        print("\n"
              "\t┌ Usage:         Argv: ┬ 1       ┬ 2     ┬ 3        ┐\n"
              "\t│                      │         │       │          │\n"
              "\t│                      │   ⚡    │  ⚡   │    ⚡    │\n"
              "\t└─────── ./get_auth.py │ API_key │ email │ password │\n"
              "\t                       └─────────┴───────┴──────────┘\n")
        exit()

    if path.exists('/tmp/.hbnb_auth_token'):
        exit()

    url = "https://intranet.hbtn.io/users/auth_token.json"

    payload = {'api_key': av[1], 'email': av[2],
               'password': av[3], 'scope': 'checker'}

    response = post(url, data=payload)

    auth = response.json()['auth_token']

    with open('/tmp/.hbnb_auth_token', 'w') as f:
        f.write(auth)

if __name__ == '__main__':
    get_auth()
