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

    elif replied == '2' or replied == 'n':
        print(Col.YELLOW + 'You answered no\n')
        time.sleep(2)

    return replied


def get_email():
    """

    """


def check_player_registered() -> bool:
    """

    """


def validate_player_email():
    """

    """


def email_not_found():
    """

    """


def create_player() -> str:
    """

    """


def check_username_suitable():
    """
    
    """


def update_worksheet_players():
    """

    """
