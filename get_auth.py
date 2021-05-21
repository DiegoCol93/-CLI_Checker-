#!/usr/bin/python3
""" Module for storing the get_auth method. """
from sys import argv as av
from requests import post
import os
from auth_user_info import API_KEY, PASS, EMAIL


def get_auth():
    """ Gets the authentication token for the current user. """
    # If wrong number of arguments were passed print usage.
    """if len(av) != 4:
        print("\n"
              "\t┌ Usage:         Argv: ┬ 1       ┬ 2     ┬ 3        ┐\n"
              "\t│                      │         │       │          │\n"
              "\t│                      │   ⚡    │  ⚡   │    ⚡    │\n"
              "\t└─────── ./get_auth.py │ API_key │ email │ password │\n"
              "\t                       └─────────┴───────┴──────────┘\n")
        exit()
    """
    if os.environ.get('HBNB_AUTH'):
        exit()

    url = "https://intranet.hbtn.io/users/auth_token.json"

    payload = {'api_key': API_KEY, 'email': EMAIL,
               'password': PASS, 'scope': 'checker'}

    response = post(url, data=payload)

    auth = response.json()['auth_token']

    env = os.environ["HBNB_AUTH"] = auth

    print(auth)

if __name__ == '__main__':
    get_auth()
