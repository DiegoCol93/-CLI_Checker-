#!/usr/bin/python3
""" Command Line Interpreter Checker Interface. """
from modules.request_correction import request_correction
from modules.show_result import show_result
from modules.get_project import get_tasks
from modules.get_auth import get_auth

from os import path, get_terminal_size
from getpass import getpass
from time import sleep
from cmd import Cmd
import json

yes_no_list = ['y', 'n', 'no', 'yes']
user_info = {}

# Color format for text printing.
y='\033[38;5;220m'  # Yellow.
g='\033[92m'  # Green.
r='\033[m'  # Reset.

# Get the size of the tty.
size = get_terminal_size()
columns = size.columns


class CLI_Checker(Cmd):
    """ Class for controling the main loop of the Checker's Console. """
    prompt = y + 'CLI-Checker ⚡ ' + r

    def preloop(self):
        """ Method that runs before the main loop of the console. """
        if path.exists('./credentials'):
            with open('./credentials', 'r') as f:
                creds = json.load(f)
                email = creds['email']
                api = creds['api']
                password = creds['password']
                get_auth(email, api, password)
        else:
            print('\033[2J', end='')
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
        # Strings for intro pre message.
        welcome_l0 = "Hi"
        welcome_l1 = "This is the"
        welcome_l2 = "CLI-Checker v0.01"
        welcome_l3 = "We hope you enjoy"
        welcome_l4 = "Please"
        welcome_l5 = "Report any issues"
        welcome_l6 = "At:"
        welcome_l7 = "https://github.com/DiegoCol93/CLI_Checker"
        welcome_l8 = "or Follow us and write to us:"
        welcome_l9 = "https://twitter.com/LopezDfelo93"
        welcome_l10 = "https://twitter.com/wisvem"
        welcome_l11 = "https://twitter.com/leovalsan_dev"

        # Calculate the space around each line's welcome message.
        welcome_s0 = ' ' * ((columns // 2) - 1 - len(welcome_l0) // 2)
        welcome_s1 = ' ' * ((columns // 2) - 1 - len(welcome_l1) // 2)
        welcome_s2 = ' ' * ((columns // 2) - 1 - len(welcome_l2) // 2)
        welcome_s3 = ' ' * ((columns // 2) - 1 - len(welcome_l3) // 2)
        welcome_s4 = ' ' * ((columns // 2) - 1 - len(welcome_l4) // 2)
        welcome_s5 = ' ' * ((columns // 2) - 1 - len(welcome_l5) // 2)
        welcome_s6 = ' ' * ((columns // 2) - 1 - len(welcome_l6) // 2)
        welcome_s7 = ' ' * ((columns // 2) - 1 - len(welcome_l7) // 2)
        welcome_s8 = ' ' * ((columns // 2) - 1 - len(welcome_l8) // 2)
        welcome_s9 = ' ' * ((columns // 2) - 1 - len(welcome_l9) // 2)
        welcome_s10 = ' ' * ((columns // 2) - 1 - len(welcome_l10) // 2)
        welcome_s11 = ' ' * ((columns // 2) - 1 - len(welcome_l11) // 2)

        welcome_l2 = "CLI-Checker" + g + " v0.01" + r

        print("\033[2;0f", end='')
        print(welcome_s0 + welcome_l0 + welcome_s0)
        sleep(2)

        print(welcome_s1 + welcome_l1 + welcome_s1)
        sleep(1.5)

        print(welcome_s2 + welcome_l2 + welcome_s2)
        sleep(1.5)

        print("\033[2;0f", end='')
        print(welcome_s3 + welcome_l3 + welcome_s3)
        sleep(1.5)

        print(welcome_s4 + welcome_l4 + welcome_s4)
        sleep(1.5)

        print(welcome_s5 + welcome_l5 + welcome_s5)
        sleep(1.5)

        print("\033[2;0f", end='')
        print(welcome_s6 + welcome_l6 + welcome_s6)
        sleep(1.5)

        print(welcome_s7 + welcome_l7 + welcome_s7)
        sleep(1.5)

        print(welcome_s8 + welcome_l8 + welcome_s8)
        sleep(1.5)

        print("\033[2;0f", end='')
        print(welcome_s9 + welcome_l9 + welcome_s9)
        sleep(1.5)

        print(welcome_s10 + welcome_l10 + welcome_s10)
        sleep(1.5)

        print(welcome_s11 + welcome_l11 + welcome_s11)
        sleep(1.5)


        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        i = 0
        print("\033[5;3f", end='')
        while i < columns - 3:
            sleep(0.02)
            print('│ ' + '▋' * i)
            print("\033[5;3f")
            i += 1
        print('\n')

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
                sleep(1)
                print('Your Credentials have been stored in' + g +
                      ' ./credentials' + r)
                sleep(2)
        get_auth(email, api, password)

    def do_project(self, arg):
        get_tasks(arg)

    def do_check(self, arg):
        task_id=request_correction(arg)
        show_result(task_id)

if __name__ == '__main__':
    CLI_Checker().cmdloop(' ┌───────────────────────────┐\n'
                          ' │     CLI-Checker ' + g + 'v0.01' + r + '     │\n'
                          ' │            by:            │\n'
                          ' │ 🔥' + y + '     Diego Lopez     ' + r + '🔥 │\n'
                          ' │ 🔥' + y + '    Wiston Venera    ' + r + '🔥 │\n'
                          ' │ 🔥' + y + '  Leonardo Valencia  ' + r + '🔥 │\n'
                          ' └───────────────────────────┘')
