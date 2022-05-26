#  Import of requirements for this project
import gspread
from tabulate import tabulate
import time
import os
import random
import validation as val
# from time import sleep
from datetime import datetime
from google.oauth2.service_account import Credentials
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
date = now.strftime("%m/%d/%Y")
score = 0
player_score = []


def logo():
    """
    Displays the logo and name to at the main menu.
    Allow user to see that it is a quiz.
    """
    clear_screen()

    print(Col.YELLOW + """
████████╗██╗░░██╗███████╗  
╚══██╔══╝██║░░██║██╔════╝  
░░░██║░░░███████║█████╗░░  
░░░██║░░░██╔══██║██╔══╝░░  
░░░██║░░░██║░░██║███████╗  
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  

░██████╗██╗███╗░░░███╗██████╗░░██████╗░█████╗░███╗░░██╗░██████╗
██╔════╝██║████╗░████║██╔══██╗██╔════╝██╔══██╗████╗░██║██╔════╝
╚█████╗░██║██╔████╔██║██████╔╝╚█████╗░██║░░██║██╔██╗██║╚█████╗░
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░░╚═══██╗██║░░██║██║╚████║░╚═══██╗
██████╔╝██║██║░╚═╝░██║██║░░░░░██████╔╝╚█████╔╝██║░╚███║██████╔╝
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░
Quiz""")

    print(Col.BLUE +
          '================================================================\n')
    print(Col.YELLOW + 'Welcome to The Simpsons Quiz!')
    print(Col.YELLOW + 'Employee: {name}\n'.format(name=val.name))
    print(Col.GREEN + 'Sponsored by:')
    print(Col.GREEN + 'Springfield Nuclear Power Plant Staff IQ Dept.')
    print(Col.GREEN + '"A smart worker prevents meltdowns"\n')
    time.sleep(2)


def clear_screen():
    """
    This function will allow the screen to be cleared
    in order to display new information such as how to play or scoreboard
    """
    os.system("cls" if os.name == "nt" else "clear")


def main_menu() -> str:
    """
    This will display the players options of
    play, scoreboard and how to play allowing them
    to choose an option.
    """
    time.sleep(1)
    print(Col.YELLOW + 'Please choose an option:')
    menu_options = '1) Play\n2) Scoreboard\n3) How to play\n4) Stats\n'
    menu_options_selected = input(menu_options)

    while menu_options_selected not in ('1', '2', '3', '4'):
        print(Col.YELLOW + 'Please select option 1, 2 or 3')
        menu_options_selected = input(menu_options)

    if menu_options_selected == '1':
        clear_screen()
        logo()
        quiz_start(questions)

    elif menu_options_selected == '2':
        clear_screen()
        logo()
        print(Col.YELLOW + 'Scoreboard:')
        print(tabulate(scoreboard_data))
        time.sleep(1)
        input(Col.YELLOW + '\nEnter any key to exit:\n')
        clear_screen()
        home()

    elif menu_options_selected == '3':
        clear_screen()
        time.sleep(1)
        how_to_play()

    elif menu_options_selected == '4':
        clear_screen()
        time.sleep(1)

    return menu_options_selected


def how_to_play():
    """
    This will display instructions on how to play to the player
    and then allow them to exit back to the main menu
    """
    print(Col.YELLOW + 'Employee: {name}\n'.format(name=val.name))
    print(Col.GREEN + 'How to Play:\n')
    time.sleep(2)
    print(Col.GREEN + 'The quiz will ask you ten (10) questions...\n')
    time.sleep(2)
    print(Col.GREEN + 'Choose answer 1, 2 or 3...\n')
    time.sleep(2)
    print(Col.GREEN + """
The questions will be about the everything
in the world of The Simpsons...\n""")
    time.sleep(2)
    print(Col.GREEN + """
Some questions will be easy for casual fans and
other questions will be hard, for the seasoned fans...\n""")
    time.sleep(2)
    print(Col.GREEN + """
You will have the option to post your score to the
scoreboard at the end.\n""")
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
    global score
    score = 0
    for sample in question_list:
        answer = input(sample.cue).lower().strip()
        if answer not in {'1', '2', '3'}:
            time.sleep(1)
            print(Col.RED + """
Wrong answer!
Please use: 1, 2 or 3 for your answer\n""")
        elif answer == sample.answer:

            score += 10
            time.sleep(1)
            print(Col.GREEN + 'Correct answer!\n')
        else:
            time.sleep(1)
            print(Col.RED + "Wrong answer!\n")

    time.sleep(1)
    clear_screen()
    score_screen()


def create_player_dict():
    player_dict = {
        'Name': val.name,
        'Score': str(score),
        'Email': val.email
    }
    print(Col.GREEN + 'Employee: ' + player_dict['Name'])
    time.sleep(2)
    print(Col.GREEN + 'Score: ' + player_dict['Score'])
    time.sleep(2)
    print(Col.GREEN + 'Email: ' + player_dict['Email'])
    time.sleep(2)
    print(Col.GREEN + 'Work Email: ' + player_dict['Name'] +
          '@SpringfieldNuclear.com\n')
    time.sleep(2)
    print(Col.GREEN +
          'Congratulations,\nyour employment has not been terminated\n')
    time.sleep(2)
    print(Col.GREEN + 'Please get back to work!')
    time.sleep(2)
    return


def score_screen():
    print(Col.GREEN + "Validating employee results")
    clear_screen()
    time.sleep(1)
    print(Col.GREEN + "Validating employee results.")
    clear_screen()
    time.sleep(1)
    print(Col.GREEN + "Validating employee results..")
    clear_screen()
    time.sleep(1)
    print(Col.GREEN + "Validating employee results...")
    print(Col.BLUE +
          '================================================================\n')
    print(create_player_dict())
    time.sleep(2)
    scoreboard_answer = input(
        Col.YELLOW + "Add score to scoreboard? Y or N\n").lower()

    if scoreboard_answer == 'y':
        time.sleep(1)
        update_scoreboard()
        return True

    elif scoreboard_answer == 'n':
        print('Thank you for playing, returning to Main Menu...')
        time.sleep(2)
        clear_screen()
        home()
        return False

    else:
        print(Col.RED + 'Please choose Y or N')
        time.sleep(1)
        score_screen()


def update_scoreboard():
    """
    This will  upload the players score to the scoreboard
    """
    print(Col.GREEN + '\nUpdating the scoreboard...\n')
    player_score.append(val.name)
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
    "What is Grandpa Simpsons first name?\n \
     1) Abraham\n \
     2) Gabriel\n \
     3) Johnny\n ",

    "What is the address of the Simpson Family?\n \
     1) 211 jebediah Street\n \
     2) 143 Shelbyville road\n \
     3) 742 Evergreen Terrace\n ",

    "Who founded Springfield?\n \
     1) Mayor Quimby\n \
     2) Jebediah Sringfield\n \
     3) Mr Burns\n ",

    "Who is the owner of Globex Corporation?\n \
     1) Mr Burns\n \
     2) Hank Scorpio\n \
     3) Ned Flanders\n ",

    "What is Moe's full name?\n \
     1) Moe Szyslak\n \
     2) Moe Murphy\n \
     3) Moe Mahony\n ",

    "What is Barney's full name?\n \
     1) Barney Stumble\n \
     2) Barney Bumble\n \
     3) Barney Gumble\n ",

    "What is Homer's favorite beer?\n \
     1) Vodka\n \
     2) Duff Beer\n \
     3) Guinness\n ",

    "Where does Homer work?\n \
     1) Springfield Area 51\n \
     2) Springfield Hydro Electric Dam\n \
     3) Springfield Nuclear Power Plant\n ",

    "What is Lenny's full name?\n \
     1) Lenny Leonard\n \
     2) Lenny Lenny\n \
     3) Lenny Lovejoy\n ",

    "What is Carls full name?\n \
     1) Carl Carlson\n \
     2) Carl Skinner\n \
     3) Carl Burns\n ",

    "What instrument does Lisa play?\n \
     1) Drums\n \
     2) Guitar\n \
     3) Saxaphone\n ",

    "What color is Barts shorts?\n \
     1) Green\n \
     2) Blue\n \
     3) Red\n ",

    "Who is Bart's best friend?\n \
     1) Nelson\n \
     2) Millhouse\n \
     3) Ralph\n ",

    "What is Millhouse's full name?\n \
     1) Millhouse O'Malley\n \
     2) Millhouse Housingtom\n \
     3) Millhouse Van Houten\n ",

    "Who owns Springfield nuclear Power Plant?\n \
     1) Mr Burns\n \
     2) Mr Smithers\n \
     3) Mayor Quimby\n ",

    "What is Mr Burns full name?\n \
     1) Jerry Alexander Burns\n \
     2) Johnny Burns\n \
     3) Charles Montgomery Burns\n ",

    "What town is rival to Springfield?\n \
     1) Shelbyville\n \
     2) Smellville\n \
     3) Acorn Creek\n ",

    "Who shot Mr Burns?\n \
     1) Homer Simpson\n \
     2) Maggie Simpson\n \
     3) Smithers\n ",

    "What does the J in Homer J Simpsons stand for?\n \
     1) Jason\n \
     2) Jerry\n \
     3) Jay\n ",

    "What is Homers' favorite food?\n \
     1) Clams\n \
     2) Ham\n \
     3) Donuts\n ",

    "Who is Barts enemy?\n \
     1) Sideshow Bob\n \
     2) Krusty the Clown\n \
     3) Ned Flanders\n ",

    "Where does Apu work?\n \
     1) Springfield Elementary School\n \
     2) Moe's Tavern\n \
     3) Kwik-E-Mart\n ",

    "What is Apu's last name?\n \
     1) Nahasapeemapetilon\n \
     2) Ram\n \
     3) Sunita\n ",

    "What nationality is Groundskeeper Willie?\n \
     1) Irish\n \
     2) Scottish\n \
     3) English\n ",

    "What are Ned Flanders sons names?\n \
     1) Steve and Stan\n \
     2) Rod and Todd\n \
     3) Jack and Jed\n ",

    "What is Barts dog called?\n \
     1) Santa's Little Helper\n \
     2) Fido\n \
     3) Barky\n ",

    "What color is Marge Simpsons hair?\n \
     1) Green\n \
     2) Black\n \
     3) Blue\n ",

    "Who is Barts Teacher?\n \
     1) Principle Skinner\n \
     2) Mrs Krabappel\n \
     3) Miss Hoover\n ",

    "What are the names of the two Aliens in the Simpsons?\n \
     1) Kling and Clonk\n \
     2) Clunk and clink\n \
     3) Kang and Kodos\n ",

    "How does Bart travel around Springfield?\n \
     1) Skateboard\n \
     2) Bicycle\n \
     3) Hoverboard\n ",
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

val.check_player()
clear_screen()
score = 0
home()
