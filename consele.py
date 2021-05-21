#!/usr/bin/python3
""" Console """
from cmd import Cmd
from modules.get_auth import get_auth
from modules.request_correction import request_correction
from modules.get_project import get_tasks
from getpass import getpass


class HBNBCommand(Cmd):
    """ HBNH console """
    prompt = '(⚡ CLI Checker ⚡) '

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

        get_auth(email, api, password)



if __name__ == '__main__':

    HBNBCommand().cmdloop('░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░')
