import gspread
import time
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
PLAYER_SHEET = SHEET.worksheet('players')

name = 'Guest'

def register_player():
    """
    Ask player for their name if they have never played previously
    """
    global name
    global player_email

    email_location = PLAYER_SHEET.col_values(2)

    time.sleep(1)
    input('What is your name?\n ')

