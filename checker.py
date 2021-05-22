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

# Color format for text printing.
y = '\033[38;5;220m'  # Yellow.
g = '\033[92m'  # Green.
r = '\033[91m' # Red
rs= '\033[m'  # Reset.

# Get the size of the tty.
size = get_terminal_size()
columns = size.columns


class CLI_Checker(Cmd):
    """ Class for controling the main loop of the Checker's Console. """

    # Class variables.
    yes_no_list = ['y', 'n', 'no', 'yes']
    tasks_dict = {}

    # Custom prompt definition.
    prompt = y + 'CLI-Checker ⚡ ' + rs

    # Overrides the preloop class method. - - - - - - - - - - - - - - - - - - |
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
            self.start_up()

    # 1st time startup method.- - - - - - - - - - - - - - - - - - - - - - - -|
    def start_up(self):
        """ Start-up method for getting and storing the user's credentials. """
        # Strings for 1st time welcome pre-message.
        welcome_l0 = "Hi"
        welcome_l1 = "This is the"
        welcome_l2 = "CLI-Checker v0.01"
        welcome_l3 = "We hope you enjoy"
        welcome_l4 = "Please"
        welcome_l5 = "Report any issues"
        welcome_l6 = "At:"
        welcome_l7 = "https://github.com/DiegoCol93/CLI_Checker"
        welcome_l8 = "or Follow us in Twitter:"
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

        # Add color for the line 2 after spaces calculation above.
        welcome_l2 = "CLI-Checker" + g + " v0.01" + rs

        # Start of printing animation...
        # \033[2;0f resets the cursor to line 2 column 0 of the terminal.
        print("\033[5;0f", end='')
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

        # Get user credentials with input box.- - - - - - - - - - - - - - - - |
        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        print("\033[6;3f", end='')
        email = str(input("Please enter your holberton e-mail: "))

        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        print("\033[6;3f", end='')
        api = str(input("Please enter your API key: "))

        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        password = getpass("\033[6;3fPlease enter your password: ")

        # Load custom mock loading Bar... - - - - - - - - - - - - - - - - - - |
        i = 0
        print("\033[6;3f", end='')
        while i < columns - 3:
            sleep(0.01)
            print('▋' * i)
            print("\033[6;3f", end='')
            i += 1
        print('\n')

        auth_status = get_auth(email, api, password)

        # If got correct authentication. - - - - - - - - - - - - - - - - - - -|
        if auth_status and 200 in auth_status:
            success = "🥳  Correct Login 🥳 "
            success_space = ' ' * ((columns // 2) - 1 - len(success) // 2)
            print("\033[5;0f", end='')
            print('┌' + '─' * (columns - 2) + '┐')
            print('│' + success_space + success + success_space + '│', end = '')
            print('└' + '─' * (columns - 2) + '┘')
            print("\033[6;3f", end='')
            question = ("Do you want to store these credentials "
                        "for future sessions Y/N?: ")
            answer = ""
            answer = str(input(question))
            while answer not in self.yes_no_list:
                print("\033[5;0f", end='')
                print('┌' + '─' * (columns - 2) + '┐')
                print('│' + ' ' * (columns - 2) + '│')
                print('└' + '─' * (columns - 2) + '┘')
                print("\033[6;3f", end='')
                answer = str(input("Please answer Yes or No: "))

            if answer.lower() in ['yes', 'y']:
                with open('./credentials', 'w+') as f:
                    json.dump({'email': email, 'api': api,
                               'password': password, 'token': ""}, f)
                    sleep(1)
                    print('Your Credentials have been stored in' + g +
                          ' ./credentials' + r)
                    sleep(2)
        elif auth_status:
            for key, value in auth_status.items():
                error = value['error']
                print(r)
                print("\033[5;0f", end='')
                print('┌' + '─' * (columns - 2) + '┐')
                print('│' + ' ' * (columns - 2) + '│')
                print('└' + '─' * (columns - 2) + '┘')
                print("\033[6;{}f".format((columns - len(error)) // 2), end='')
                print(error + rs)
            self.start_up()

        else:
            return False

    # Project command - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_project(self, arg):
        self.tasks_dict = get_tasks(arg)

    # Check command - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_check(self, arg):
        # If tasks dictionary is empty try reading from project file.
        tasks_dict = self.tasks_dict
        if bool(tasks_dict) is None:
            try:
                with open('./current_project') as f:
                    self.tasks_dict = json.loads()
            except Exception as e:
                print(r + './current_project' + rs +' does not exist.')
                print('If you continue having this problem,')
                print('Please run project command / help project.')
                print('To cache the current project id #')
        else:
            self.task_id = request_correction(arg)
            show_result(self.task_id, self.tasks_dict)

    def do_EOF(self, arg):
        """ Exits console when receiving an EOF. """
        return True

    def emptyline(self):
        """ Overwriting the emptyline method. """
        return False

    def do_quit(self, arg):
        """ Quit command to exit the console. """
        return True

if __name__ == '__main__':
    CLI_Checker().cmdloop(' ┌───────────────────────────┐\n'
                          ' │     CLI-Checker ' + g + 'v0.01' + rs + '     │\n'
                          ' │            by:            │\n'
                          ' │ 🔥' + y + '     Diego Lopez     ' + rs + '🔥 │\n'
                          ' │ 🔥' + y + '    Wiston Venera    ' + rs + '🔥 │\n'
                          ' │ 🔥' + y + '  Leonardo Valencia  ' + rs + '🔥 │\n'
                          ' └───────────────────────────┘')
