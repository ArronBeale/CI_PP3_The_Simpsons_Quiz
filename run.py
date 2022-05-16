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
    print(Col.YELLOW + 'Please choose an option:\n')
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
        time.sleep(1)
        how_to_play()

    return menu_options_selected


def how_to_play():
    """
    This will display instructions on how to play to the player
    """
    print(Col.YELLOW + 'How to Play:\n')
    time.sleep(2)
    print(Col.YELLOW + 'The quiz will ask you ten (10) questions...\n')
    time.sleep(2)
    print(Col.YELLOW + 'Choose answer 1, 2 or 3...\n')
    time.sleep(2)
    print(Col.YELLOW + 'The questions will be about the characters and the world of The Simpsons...\n')
    time.sleep(2)
    print(Col.YELLOW + 'Some questions will be easy for casual fans and other questions will be hard, for the seasoned fans...\n')
    time.sleep(2)
    print(Col.YELLOW + 'You will have the option to post your score to the scoreboard at the end.\n')
    time.sleep(2)
    print(Col.YELLOW + 'Have fun!\n')
    time.sleep(2)
    print(Col.YELLOW + "D'oH!\n")
    
    input('Enter any key to exit: \n')
    clear_screen()
    home()


def home():
    """
    Logo and main menu functions combined in this function as a home function
    """
    logo()
    main_menu()


class Question:
    """
    Questions instance, gets question
    and answer
    """
    def __init__(self, cue, answer):
        self.cue = cue
        self.answer = answer


question_cues = [
    "Question 1 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 2 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 3 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 4 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 5 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 6 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 7 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 8 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 9 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 10 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 11 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 12 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 13 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 14 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 15 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 16 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 17 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 18 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 19 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 20 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 21 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 22 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 23 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 24 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 25 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 26 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 27 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 28 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 29 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",

     "Question 30 place holder text\n \
     1)Answer 1 place holder text\n \
     2)Answer 2 place holder text\n \
     3)Answer 3 place holder text\n ",
]

home()
