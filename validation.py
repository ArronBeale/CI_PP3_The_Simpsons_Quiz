import gspread
import time
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from colors import Color as Col


# Scope and constant variables for google api and sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('scoreboard')
PLAYER_SHEET = SHEET.worksheet('players')


def get_email():
    """
    Ask player to input email
    """
    global email
    email = input(Col.YELLOW + 'What is your email address?\n ')
    time.sleep(1)
    return email


def check_player() -> str:
    """
    Check if player has registered previously
    """
    time.sleep(1)
    print(Col.YELLOW + 'Is this your first visit?\n')
    reply = '1) Yes \n2) No\n'
    replied = input(reply).lower()

    while replied not in ('1', 'y', '2', 'n'):
        print(Col.YELLOW + 'Please choose an option:')
        replied = input(reply).lower()
        time.sleep(1)

    if replied == '1' or replied == 'y':
        print(Col.YELLOW + 'You answered yes\n')
        time.sleep(2)
        get_email()
        time.sleep(1)
        print(Col.YELLOW + f'Your email is {email}\n')
        validate_player_email(email)
        retrieve_player_name()

    elif replied == '2' or replied == 'n':
        print(Col.YELLOW + 'You answered no\n')
        time.sleep(2)
        get_email()
        validate_player_email(email)
        retrieve_player_name()

    return replied


def retrieve_player_name():
    """
    This function will search database for the players email submitted on
    a previous visit and retrieve their name to greet them
    """
    player_email_row = PLAYER_SHEET.find(email).row
    player_name = PLAYER_SHEET.row_values(player_email_row)[0]
    print(f'\nWelcome back {player_name}')
    time.sleep(2)
    return player_name


def validate_player_email(email: str):
    """
    Validate player email address.
    Must be in format of name@example.com
    @param email(string): Player's email address
    """
    try:
        validate_email(email)
        return True

    except EmailNotValidError as e:
        print(Col.RED + "\n" + str(e))
        print(Col.RED + "Please try again.\n")
        get_email()
