import gspread
import time
import os
import random
import pprint
import validation as val
from time import sleep
from datetime import datetime
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
SCOREBOARD = SHEET.worksheet('scores')
PLAYER_SHEET = SHEET.worksheet('players')

scoreboard_data = SCOREBOARD.get_all_values()

now = datetime.now()
date = now.strftime("%m/%d/%Y, %H:%M:%S")
name = ''
email = ''
score = 0
player_score = []


def player_login():
    """
    This will allow the player to login if they have registered previously
    """
    global name
    name = input(Col.YELLOW + 'What is your name?\n')

    try:
        if len(name) < 3 or len(name) > 12:
            raise ValueError(
                'Name needs to be at least 3 characters or maximum 12 characters'
            )
    except ValueError as e:
        print(Col.RED + f'Invalid name length: {e},\nplease try again.\n')
        time.sleep(1)
        player_login()

    player_score.append(name)
    time.sleep(1)
    clear_screen()
    print(Col.YELLOW + f'\nWelcome {name}\n')
    time.sleep(2)


def logo():
    """
    Displays the logo and name
    """
    clear_screen()

    print(Col.YELLOW + """
        
  _______ _             _____ _                                        ____        _     
 |__   __| |           / ____(_)                                      / __ \      (_)    
    | |  | |__   ___  | (___  _ _ __ ___  _ __  ___  ___  _ __  ___  | |  | |_   _ _ ____
    | |  | '_ \ / _ \  \___ \| | '_ ` _ \| '_ \/ __|/ _ \| '_ \/ __| | |  | | | | | |_  /
    | |  | | | |  __/  ____) | | | | | | | |_) \__ \ (_) | | | \__ \ | |__| | |_| | |/ / 
    |_|  |_| |_|\___| |_____/|_|_| |_| |_| .__/|___/\___/|_| |_|___/  \___\_\\__,_|_/___|
                                         | |                                             
                                         |_|                                             
""")

    
    print(Col.BLUE + '=============================================================================================\n')
    print(Col.YELLOW + 'Welcome to The Simpsons Quiz!')
    print(Col.YELLOW + f'Employee: {name}\n')
    print(Col.GREEN + 'Sponsored by:')
    print(Col.GREEN + 'Springfield Nuclear Power Plant Staff IQ Dept.')
    print(Col.GREEN + '"A smart worker prevents meltdowns"\n')
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
        quiz_start(questions)

    elif menu_options_selected == '2':
        clear_screen()
        logo()
        print(scoreboard_data)
        time.sleep(1)
        input(Col.YELLOW + '\nEnter any key to exit:\n')
        clear_screen()
        home()

    elif menu_options_selected == '3':
        clear_screen()
        time.sleep(1)
        how_to_play()

    return menu_options_selected


def how_to_play():
    """
    This will display instructions on how to play to the player
    """
    print(Col.YELLOW + f'Employee: {name}\n')
    print(Col.GREEN + 'How to Play:\n')
    time.sleep(2)
    print(Col.GREEN + 'The quiz will ask you ten (10) questions...\n')
    time.sleep(2)
    print(Col.GREEN + 'Choose answer 1, 2 or 3...\n')
    time.sleep(2)
    print(Col.GREEN + 'The questions will be about the everything \nin the world of The Simpsons...\n')
    time.sleep(2)
    print(Col.GREEN + 'Some questions will be easy for casual fans and \nother questions will be hard, for the seasoned fans...\n')
    time.sleep(2)
    print(Col.GREEN + 'You will have the option to post your score to the \nscoreboard at the end.\n')
    time.sleep(2)
    print(Col.GREEN + 'Have fun!\n')
    time.sleep(2)
    print(Col.GREEN + "D'oH!\n")

    input(Col.YELLOW + 'Enter any key to exit:\n')
    clear_screen()
    home()


def home():
    """
    Logo and main menu functions combined in this function as a home function
    """
    logo()
    main_menu()


def quiz_start(questions):
    """
    Start the quiz, track score and select random questions
    """
    question_list = random.sample(questions, 10)

    for sample in question_list:
        answer = input(sample.cue).lower().strip()
        if answer not in {'1', '2', '3'}:
            time.sleep(1)
            print(Col.RED + "Wrong answer!\n Please use: 1, 2 or 3 for your answer\n")
        elif answer == sample.answer:
            global score
            score += 10
            time.sleep(1)
            print(Col.GREEN + 'Correct answer!\n')
        else:
            time.sleep(1)
            print(Col.RED + "Wrong answer!\n")

    time.sleep(1)
    clear_screen()
    score_screen()


def score_screen():    
    print(Col.YELLOW + f"Your score is: {score}\n")
    time.sleep(2)
    scoreboard_answer = input(
        Col.YELLOW + "Add score to scoreboard? Y or N\n").lower()

    if scoreboard_answer == 'y':
        time.sleep(1)
        update_scoreboard()

    elif scoreboard_answer == 'n':
        print('Thank you for playing, returning to Main Menu...')
        time.sleep(2)
        clear_screen()
        home()

    else:
        print(Col.RED + 'Please choose Y or N')
        time.sleep(1)
        score_screen()


def update_scoreboard():
    """
    This will  upload the players score to the scoreboard
    """
    print(Col.GREEN + '\nUpdating the scoreboard...\n')
    player_score.append(score)
    player_score.append(date)
    time.sleep(2)
    SCOREBOARD.append_row(player_score)
    print(Col.GREEN + '\nScoreboard has been updated\n')
    time.sleep(2)
    input(Col.YELLOW + '\nEnter any key to exit:\n')
    clear_screen()
    home()


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

questions = [
    Question(question_cues[0], "1"),
    Question(question_cues[1], "3"),
    Question(question_cues[2], "2"),
    Question(question_cues[3], "2"),
    Question(question_cues[4], "1"),
    Question(question_cues[5], "3"),
    Question(question_cues[6], "2"),
    Question(question_cues[7], "3"),
    Question(question_cues[8], "1"),
    Question(question_cues[9], "1"),
    Question(question_cues[10], "3"),
    Question(question_cues[11], "2"),
    Question(question_cues[12], "2"),
    Question(question_cues[13], "3"),
    Question(question_cues[14], "1"),
    Question(question_cues[15], "3"),
    Question(question_cues[16], "1"),
    Question(question_cues[17], "2"),
    Question(question_cues[18], "3"),
    Question(question_cues[19], "3"),
    Question(question_cues[20], "1"),
    Question(question_cues[21], "3"),
    Question(question_cues[22], "1"),
    Question(question_cues[23], "2"),
    Question(question_cues[24], "2"),
    Question(question_cues[25], "1"),
    Question(question_cues[26], "3"),
    Question(question_cues[27], "2"),
    Question(question_cues[28], "3"),
    Question(question_cues[29], "1"),

]

player_login()
clear_screen()
home()

