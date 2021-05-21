#!/usr/bin/python3
""" Console """
from cmd import Cmd
from modules.request_correction import request_correction
from modules.show_result import show_result
from modules.get_project import get_tasks
from modules.get_auth import get_auth
from getpass import getpass
import json

from os import path, get_terminal_size

yes_no_list = ['y', 'n', 'no', 'yes']
user_info = {}

y='\033[38;5;220m'
r='\033[m'

class CLI_Checker(Cmd):
    """ Checker Console. """
    prompt = y + 'CLI-Checker ⚡ ' + r

    def preloop(self):
        if path.exists('./credentials'):
            return
        self.do_start()

    def do_EOF(self, arg):
        """ Exits console when receiving an EOF. """
        return True

    def emptyline(self):
        """ Overwriting the emptyline method. """
        return False

    def do_quit(self, arg):
        """ Quit command to exit the console. """
        return True

    def do_start(self):
        """ Start-up method for getting and storing the user's credentials. """
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
        task_id=request_correction(arg)
        show_result(task_id)

if __name__ == '__main__':

    size = get_terminal_size()
    col = size.columns
    # CLI_Checker().cmdloop('┌' + '─' * (col - 2) + '┐')

    CLI_Checker().cmdloop(' ┌───────────────────────────┐\n'
                          ' │     CLI-Checker v0.01     │\n'
                          ' │            by:            │\n'
                          ' │' + y + '        Diego Lopez        ' + r + '│\n'
                          ' │' + y + '       Wiston Venera       ' + r + '│\n'
                          ' │' + y + '     Leonardo Valencia     ' + r + '│\n'
                          ' └───────────────────────────┘')
