import gspread
import time
import os
import random
import validation as val
from time import sleep
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from colors import Color as Col

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scoreboard')


def logo():
    """
    Displays the logo and name
    """
    print(Col.YELLOW + '\n#######                   #####                                                  #####                  ')
    print(Col.YELLOW + '   #    #    # ######    #       # #    # #####   ####   ####  #    #  ####     #     # #    # # ###### ')
    print(Col.YELLOW + '   #    #    # #         #       # ##  ## #    # #      #    # ##   # #         #     # #    # #     #  ')
    print(Col.YELLOW + '   #    ###### #####      #####  # # ## # #    #  ####  #    # # #  #  ####     #     # #    # #    #   ')
    print(Col.YELLOW + '   #    #    # #               # # #    # #####       # #    # #  # #      #    #   # # #    # #   #    ')
    print(Col.YELLOW + '   #    #    # #               # # #    # #      #    # #    # #   ## #    #    #    #  #    # #  #     ')
    print(Col.YELLOW + '   #    #    # ######     #####  # #    # #       ####   ####  #    #  ####      #### #  ####  # ######\n')
    print(Col.BLUE + '===========================================================================================================\n')
    print(Col.YELLOW + 'Welcome to The Simpsons Quiz!\n')
    print(Col.GREEN + 'Sponsored by:')
    print(Col.GREEN + 'Springfield Nuclear Power Plant,')
    print(Col.GREEN + '100 Industrial Way,')
    print(Col.GREEN + 'Springfield\n')
    time.sleep(1)


def clear_screen():
    """
    This function will allow the screen to be cleared as player navigates
    """
    os.system("cls" if os.name == "nt" else "clear")

def main_menu() -> str:
    """
    This will display the players options of play, scoreboard and how to play
    """
    time.sleep(1)
    print(Col.YELLOW + 'Please choose an option:')
    menu_options = '1) Play\n2) Scoreboard\n3) How to play\n\n'
    menu_options_selected = input(menu_options)

    while menu_options_selected not in ('1', '2', '3'):
        print(Col.YELLOW + 'Please select option 1, 2 or 3')
        menu_options_selected = input(menu_options)

    if menu_options_selected == '1':
        clear_screen()
        logo()

    elif menu_options_selected == '2':
        clear_screen()
        logo()

    elif menu_options_selected == '3':
        clear_screen()
        logo()

    return menu_options_selected


logo()
main_menu()
