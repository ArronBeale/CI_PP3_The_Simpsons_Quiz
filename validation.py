#  Import of requirements for this project
import gspread
import time
import os
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from colors import Color as Col


#  Scope and constant variables for google api and sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


#  Constants for credentials to authorise access to database
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('scoreboard')
PLAYER_SHEET = SHEET.worksheet('players')
SCORE_SHEET = SHEET.worksheet('scores')

name = ''
email = ''
player_creds = []


def check_player() -> str:
    """
    Checks if player has played previously,
    Calls on get email function and validate email function
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
        print(Col.YELLOW + f'\nYour email is {email}\n')
        time.sleep(1)
        player_login()
        register_new_player()
        return True

    elif replied == '2' or replied == 'n':
        print(Col.YELLOW + 'You answered no\n')
        time.sleep(2)
        get_email()
        validate_player_email(email)
        retrieve_player_name()
        return False


def get_email():
    """
    This will ask player to input their email address.
    """
    global email
    email = input(Col.YELLOW + 'What is your email address?\n ')
    time.sleep(1)
    validate_player_email(email)
    return email, True

#  The below function uses code from the email_validator library


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
        return False


def register_new_player():
    """
    This function will add new players email and name to players database
    in order to allow them to be remembered when they visit again.
    """
    player_creds.append(name)
    player_creds.append(email)
    PLAYER_SHEET.append_row(player_creds)


def retrieve_player_name():
    """
    This function will search database for the players email submitted on
    a previous visit and retrieve their name to greet them and use the name.
    """
    global name
    global player_name
    try:
        player_email_row = PLAYER_SHEET.find(email).row
        player_name = PLAYER_SHEET.row_values(player_email_row)[0]
        clear_screen()
        print(Col.GREEN + f'Welcome,\nEmployee: {player_name}\n')
        time.sleep(2)
        print(Col.GREEN +
              'Please complete your daily mandatory IQ test\n')
        time.sleep(2)
        input(Col.GREEN + '\nEnter any key to continue:\n')
        time.sleep(1)

        name = player_name
        return player_name, True

    except AttributeError:
        print('\nEmail not found in past player records, adding now')
        time.sleep(3)
        player_login()


def player_login():
    """
    This function will ask player for their name in order
    to register them for when they return in the future
    """
    global name
    name = input(Col.YELLOW + '\nWhat is your name?\n')

    try:
        if len(name) < 3 or len(name) > 12:
            raise ValueError(
                """Name needs to be at least 3 characters
                or maximum 12 characters"""
            )

    except ValueError as e:
        print(Col.RED + f'Invalid name length: {e},\nplease try again.\n')
        time.sleep(1)
        player_login()
        return False

    time.sleep(1)
    clear_screen()
    print(Col.GREEN + f'Welcome,\nEmployee: {name}\n')
    time.sleep(2)
    print(Col.GREEN +
          'Please complete your daily mandatory IQ test\n')
    time.sleep(2)
    input(Col.GREEN + '\nEnter any key to continue:\n')
    register_new_player()
    time.sleep(1)


def validating_message():
    """
    Displays the message that validation of players
    score is in progress.
    """
    print(Col.GREEN + "Validating employee results")
    print(Col.BLUE +
          '================================================================\n')
    time.sleep(1)
    clear_screen()
    print(Col.GREEN + "Validating employee results.")
    print(Col.BLUE +
          '================================================================\n')
    time.sleep(1)
    clear_screen()
    print(Col.GREEN + "Validating employee results..")
    print(Col.BLUE +
          '================================================================\n')
    time.sleep(1)
    clear_screen()
    print(Col.GREEN + "Validating employee results...")
    print(Col.BLUE +
          '================================================================\n')
    time.sleep(1)


def total_players():
    """
    This functions will loop through each column of the players sheet
    and add each player to get a sum the of total number of players
    that have visited.
    """
    player_list = PLAYER_SHEET.col_values(1)
    total_players = 0
    x = 1
    for x in player_list:
        total_players += 1
    return total_players


def total_score():
    """
    This function will calculate the total combined score of all player scores
    that have been recorded in the scores database.
    It will deduct Mr Burns score of 9999, and add 100 as Homers score is -100,
    these scores are easter eggs that should be not be included in the final
    total.
    """
    score_column = SCORE_SHEET.col_values(2)
    total_players_score = 0

    del score_column[0]
    score_column = list(map(int, score_column))

    for score in score_column:
        total_players_score += score

    #  This removes Mr Burns score of 9999 from final number
    total_players_score -= 9999

    #  This adds 100 to compensate for Homers' score of -100
    total_players_score += 100

    return total_players_score


def total_players_submit():
    """
    This functions will loop through each column of the scores sheet
    and add each player to get a sum of the total number of players
    that have submitted to the scoreboard.
    """
    player_list = SCORE_SHEET.col_values(1)
    total_player_submitted = 0
    x = 1
    for x in player_list:
        total_player_submitted += 1

    return total_player_submitted


def average_score():
    """
    This will calculate the avergae score of all
    the players who have played so far.
    it will exclude the Easter eggs scores of Mr Burns and Homer.
    """
    return int(total_score() / total_players_submit())


def clear_screen():
    """
    This function will allow the screen to be cleared
    in order to display new information such as how to play or scoreboard
    """
    os.system("cls" if os.name == "nt" else "clear")
