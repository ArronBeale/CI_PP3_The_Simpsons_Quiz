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
    print('Welcome to The Simpsons Quiz!\n')
    print(Col.GREEN + 'Sponsored by:')
    print(Col.GREEN + 'Springfield Nuclear Power Plant,')
    print(Col.GREEN + '100 Industrial Way,')
    print(Col.GREEN + 'Springfield\n')


logo()
