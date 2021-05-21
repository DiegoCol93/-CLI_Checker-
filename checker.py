#!/usr/bin/python3
""" Console """
from cmd import Cmd
from modules.get_auth import get_auth
from modules.request_correction import request_correction
from modules.get_project import get_tasks
from modules.show_result import show_result
from getpass import getpass
import json
import os

yes_no_list = ['y', 'n', 'no', 'yes']
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
user_info = {}


class HBNBCommand(Cmd):
    """ HBNH console """
    prompt = '(⚡ CLI Checker ⚡) '

    def preloop(self):
        if os.path.exists('./credentials'):
            return
        self.do_start

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_start(self, arg):
        """\n""" \
            """\t┌ Usage:         Argv: ┬ 1       ┬ 2     ┬ 3        ┐\n """ \
            """\t│                      │         │       │          │\n """ \
            """\t│                      │   ⚡    │  ⚡   │    ⚡    │\n """ \
            """\t└───────    auth.py    │ API_key │ email │ password │\n """ \
            """\t                       └─────────┴───────┴──────────┘\n """
        email = str(input("Please enter your mail: "))
        api = str(input("Please enter your API key: "))
        password = getpass("Please enter your password: ")
        answer = ""
        question = ("Do you want to store this credentials"
                    " for future sessions Yes/No?: ")
        while answer not in yes_no_list:
            answer = str(input(question))
        if answer.lower() in ['yes', 'y']:
            with open('./credentials', 'w+') as f:
                json.dump({'email': email, 'api': api,
                           'password': password, 'token': ""}, f)
        get_auth(email, api, password)

    def do_project(self, arg):
        get_tasks(arg)

    def do_check(self, arg):
        show_result(request_correction(arg))

if __name__ == '__main__':

    HBNBCommand().cmdloop('░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░')
