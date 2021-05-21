#!/usr/bin/python3
""" Module for getting authentication token for the user. """
from requests import post
from sys import argv as av
from os import environ

if len(av) != 4:
    print("\n\tUsage: ./get_auth.py <API key> <holberton email> <password>\n")
    exit()

payload = { 'api_key': av[1],
            'email': av[2],
            'password': av[3],
            'scope': 'checker' }

response = post("https://intranet.hbtn.io/users/auth_token.json", data=payload)

print(response.json())
