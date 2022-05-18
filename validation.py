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


def player_login():
    """
    This will allow the player to login if they have registered previously
    """


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

