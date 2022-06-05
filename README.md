# The Simpsons Quiz


![cover image](https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/cover.PNG)
Developer: Arron Beale  

[Deployed Site](https://the-simpsons-quiz.herokuapp.com/)  
(Note: Ctrl + click to open in a new tab)    


## Table of Content
1. [Project Goals](#project-goals)
   1. [User Goals](#user-goals)
   2. [Site owner Goals](#site-owner-goals)
2. [User Experience](#User-Experience)
   1. [Target Audience](#target-audience)
   2. [User Requirements and Expectations](#user-requirments-and-expectations)
   3. [Manual](#manual)
   4. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
   1. [Flowcharts](#flowcharts)
   2. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
   1. [Languages](#Languages)
   2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
7. [PEP8 Validation](#pep8-validation)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#ackowledgements)

## Project Goals

### User Goals
- To play a fun quiz game based on The Simpsons
- To test my knowledge of The Simpsons world
- The site remembers me on my next visit
- My score is recorded to a scoreboard

### Site Owner Goals
- To provide a fun quiz to users
- To register new players and remember previous players
- To provide a how to play screen
- To ensureplayers get feedback while playing

[Back to Top](<#table-of-content>)
## User Experience

### Target Audience
- The target audience for The Simpsons Quiz is
anyone who is a fan of the show and from ages 10 years and older.

### User Requirments and Expectations
- A fun and engaging quiz
- Intuitive navigation and flow throughout
- Ability to save score to a scoreboard
- Name is remembered on next visit
- Ability to view a scoreboard of past players

## Manual
<details><summary>Click here to view the manual</summary>
 
 ### Player Validation
 - Upon running the game the player will be asked if they have played before. 
 - New  players will be registered into the players database using their submitted email and name.
 - Returning players will be asked for their email address and their name will be taken from the Players Database to greet them.

 ### Main Menu
 - The Main Menu consists of 4 options to choose from:
   1) Play
   2) Scoreboard
   3) How to Play
   4) Stats
- Choose an option using numbers 1, 2, 3 and 4

### Play
 - From the Main Menu input select option 1 to begin playing. This will begin the quiz. Ten (10) random questions will be asked, ther will be 3 options, one of which will be the correct answer.

 - Upon completion of the quiz the player will be brought to their results screen which will give the final score. The player will be asked to choose to add score the sacore to the scoreboard, Yes (Y) or No (N). After an option is chosen and if the score ahs or has not been added the player will e brought back to the main menu.


### Scoreboard
 - From the Main Menu select option 2 to view the scoreboard. This will bring the player to the scoreboard screen and display the scores of all past players.

### How to Play
 - Fron the Main Menu select option 3 to learn how to play. This will bring the player to the how to play screen, all the information on how to play will be displayed here.

### Stats
 - From the Main Menu select option 4, this will bring the player to the stats screen. Here you will find statistics such as, total players so far, total combined score and average score of all players so far.
 

 </details>
 

[Back to Top](<#table-of-content>)  
## User Stories

### First Time User
1. As a player, I would like to know how to play.
2. As a player, I would like to have a main menu.
3. As a player, I would like to register my name and email for future visits.
4. As a player, I would like to upload my score to a scoreboard.
5. As a player, I would like to see statistics.

### Returning User
6. As a returning player, I would like to be remembered.
7. As a returning player, I would like to view a scoreboard.
 
### Site Owner
8. As the site owner, I would like the game to be challenging and fun.
9. As the site owner, I would like an eye catching logo.
10. As the site owner, I would like some humor on the main menu.
11. As the site owner, I would like valid data from the player especially correct email formats.
12. As the site owner, I would like a database of player scores, names and emails.
13. As the site owner, i would like to give the option for a player to submit their score or not.
 
[Back to Top](<#table-of-content>)
## Technical Design


### Flow Charts

<details><summary>Main Menu</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/flowcharts/flow-main-menu.png">
</details>

<details><summary>Questions</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/flowcharts/flow-questions.png">
</details>

<details><summary>Scoreboard</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/flowcharts/flow-scoreboard.png">
</details>

### Wireframes

<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/wireframes/wireframe-main.png">
</details>

   
[Back to Top](<#table-of-content>)
## Technologies Used

### Languages
- [Python](https://www.python.org/)


### Frameworks and Tools
- [Balsamiq](https://balsamiq.com/)

- [FlatIcon](https://www.flaticon.com/)

- [GitPod](https://gitpod.io/)

- [Git](https://git-scm.com/)

- [GitHub](https://github.com/)

- [Google Cloud Platform](https://cloud.google.com/cloud-console/)

[Back to Top](<#Table-of-Content>)

### Libraries

#### Python Libraries
- [OS](https://docs.python.org/3/library/os.html)
- [Random](https://docs.python.org/3/library/random.html)
- [PyColors](https://pypi.org/project/pycolors/)
- [Date time](https://docs.python.org/3/library/datetime.html)
- [Tabluate](https://pypi.org/project/tabulate/)
- [Time](https://docs.python.org/3/library/time.html)
- [Unittest](https://docs.python.org/3/library/unittest.html)

#### Third Party Libraries
- [Gspread](https://docs.gspread.org/en/v5.3.2/)
  - Justification: Used to work with Google Sheets data to record scores and emails of players.
- [Email validator](https://pypi.org/project/email-validator/)
  - Justification: Used to ensure email addresses provided were valid and had the correct format required.
- [Google Auth](https://google-auth.readthedocs.io/en/master/)
  - Justification: Used to link the Google API in order to be authorised to access and edit the Google Sheets.

## Features

### Quiz
- A fun and challengibng quiz for all fans of The Simpsons.
- Contains a variety of questions related to The Simpsons.
- User stories covered:
<details><summary>Quiz image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_quiz.PNG">
</details>  


### Validate New Player
- Asks if player has played before
- New players will be prompted to input their email and name to be stored for future visits and for the scoreboard.
- User stories covered:
<details><summary>Validate New Player Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_new_player.PNG">
</details>  


### Validate returning Player
- Asks returning players for their email and will then extract their name from the player database.
- User stories covered:
<details><summary>Validate returning Player Image
</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_returning_player.PNG">
</details>  


### Validate and Greet Name
- Will greet players by their name after validation has completed.
- User stories covered:
<details><summary>Validate and Greet Name Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_greet_name.PNG">
</details>  


### Main Menu
- Contains the logo for the quiz.
- Home to options: play, scoreboard, how to play and stats.
- User stories covered:
<details><summary>Main Menu Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu2.PNG">
</details>  


### Logo
- A large ascii art logo in yellow to reflect the image of The Simpsons.
- User stories covered:
<details><summary>Logo Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu.PNG">
</details>  


### How to Play
- Displays to the player how to play the quiz.
- User stories covered:
<details><summary>User stories covered</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_how_to_play.PNG">
</details>  


### Scoreboard
- Displays the scoreboard of all past players who have chosen to upload their score.
- User stories covered:
<details><summary>Scoreboard Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_scoreboard.PNG">
</details>  


### Add to Scoreboard
- Gives the option to add their score to the scoreboard.
- User stories covered:
<details><summary>Add to Scoreboard Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_add_to_scoreboard.PNG">
</details>  


### Player Database
- Stores the player names and email addresses to a Google Sheet.
- User stories covered:
<details><summary>Players Database Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_player_database.PNG">
</details>  


### Scoreboard Database
- Stores player name and score to a Google Sheet.
- User stories covered:
<details><summary>Scoreboard Database Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_scoreboard_database.PNG">
</details>  


### Results
- Displays player score, name and email after the quiz has ended.
- User stories covered:
<details><summary>Results Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_results.PNG">
</details>  


### Stats
- Displays a statistics screen that shows total players, total combined score and average score of players.
- User stories covered:
<details><summary>Stats Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_stats.PNG">
</details>  


[Back to Top](<#table-of-content>)
## Validation


### PEP8 Validation
<details><summary>run.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/validation/validation_pep8_run.PNG">
</details>

<details><summary>validation.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/validation/validation_pep8_validation.PNG">
</details>

<details><summary>test_validation.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/validation/validation_pep8_test_validation.PNG">
</details>  


## Testing

### Manual Testing

<details><summary>View manual testing</summary>

### Testing User Stories

First Time User:
1. As a player, I would like to know how to play.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Select option 3 | You are taken to the how to play screen | As expected |
| How to Play | View displayed information | Information on the how to play screen should be visible | As expected |
<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu2.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_how_to_play.PNG?raw=true">
</details>

2. As a player, I would like to have a main menu.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Run game and follow prompts which will bring you to main menu | | As expected |

<details><summary>Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu.PNG">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu2.PNG?raw=true">
</details>

3. As a player, I would like to register my name and email for future visits.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Validate New Player | When programme runs select option 1, you have not played before, input email and name when prompted | Name and email will be recorded for future visits| As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_validate_new_player.PNG?raw=true">
</details>

4. As a player, I would like to upload my score to a scoreboard.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add to Scoreboard| When quiz ends, select Yes to upload to the scoreboard | Score will upload to scoreboard | As expected |
| Scoreboard | After submitting score select option 2 in main menu | Scoreboard will be shown, your score listed | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_add_to_scoreboard.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_scoreboard.PNG?raw=true">
</details>

5. As a player, I would like to see statistics.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | From main menu select option 4 | Statistics screen will load | As expected |
| Stats | From selectiing stats from main menu stats screen will now display statistics | Total players, total score and average score will be displayed| As expected |
<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu2.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_stats.PNG?raw=true">
</details>

Returning User
6. As a returning player, I would like to be remembered.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Validate Returning Player| When programme runs select option 2, you have played before | Input email when prompted, name will be retrieved from the database | As expected |
| Validate and Greet Name| After validation player will be greeted by name | Player name will be displayed in a welcome message | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_validate_returning_player.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_validate_greet_name.PNG?raw=true">
</details>

7. As a returning player, I would like to view a scoreboard.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Scoreboard | From the main menu select option 2 to display the scoreboard | Scoreboard will be shown | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_scoreboard.PNG?raw=true">
</details>

Site Owner
8. As the site owner, I would like the game to be challenging and fun.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Quiz | From the main menu select option 1 to start the quiz | Quiz will begin | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu2.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_quiz.PNG?raw=true">
</details>

9. As the site owner, I would like an eye catching logo.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Logo | Run programme and advance as prompted to be brought to main menu where logo is located | Logo will be displayed | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu.PNG?raw=true">
</details>

10. As the site owner, I would like some humor on the main menu.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Run programme and advance as prompted to be brought to main menu | find player name listed as employee of Springfield Nuclear Power Plant and a sponsor message from Staff IQ Department | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_main_menu.PNG?raw=true">
</details>

11. As the site owner, I would like valid data from the player especially correct email formats.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Validate Player | Enter incorrect email format | Error is displayed to enter correct format  | As expected |
| Validate Player | Enter incorrect name format, less than 3 chars or more than 12 | | |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_validate_returning_player2.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_validate_returning_player3.PNG?raw=true">
</details>

12. As the site owner, I would like a database of player scores, names and emails.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Player Database | Restricted access due to sensitive information | Database contains Player names and emails | As expected |
| Scoreboard Database | Restricted access due to sensitive information | Database contains Player scores | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_player_database.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_scoreboard_database.PNG?raw=true">
</details>

13. As the site owner, i would like to give the option for a player to submit their score or not.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add to Scoreboard| When quiz ends, select Yes or No to upload to the scoreboard | Score will or will not upload to scoreboard depending on choice | As expected |
| Scoreboard | After submitting score select option 2 in main menu | Scoreboard will be shown, your score listed | As expected |

<details><summary>Images</summary>
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_add_to_scoreboard.PNG?raw=true">
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/features/feature_scoreboard.PNG?raw=true">
</details>
</details>


### Automated Testing
 
 <details><summary>View automated testing</summary>

- Automated testing was done using the unittest and coverage librararies for Python.


### Unit Tests
- Functions tested were for email validation for correct format of emails submitted by the user.

<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_unit_tests1.PNG?raw=true">

- Test ran and passed with the correct email format submitted for the test.

<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_unit_tests2.PNG?raw=true">

- Test failed when an incorrect format was submitted into the test.

<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_unit_tests4.PNG?raw=true">

<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_unit_tests3.PNG?raw=true">

- Tests were also created to for calculating the total number of players so far, the total combined score of all scores submitted and the average score of players. Each test was limited to one assertion in order to easily identify any test that might fail.

<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_unit_tests1.PNG?raw=true">


### Coverage 

- Coverage was installed via the terminal, pip install coverage
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_coverage1.PNG?raw=true">


- Coverage was then used to test using the following command, coverage run test_validation.py
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_coverage2.PNG?raw=true">


- The results of the test were the following:
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_coverage3.PNG?raw=true">

- A HTML report was also generated using the command, coverage html
<img src="https://github.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/blob/main/docs/validation/validation_coverage4.PNG?raw=true">

</details>






[Back to Top](<#table-of-content>)
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Player name not displaying in menu | Name variable refrenced in validation.py so needed to be imported and referenced as val.name|
| Stats function not calculating total score | Fucnction was given the players database and not the scores database, corrected by directing function to scores database |
| Logo too big for terminal | A new logo was chosen as the original was far too big to fit into the terminal |
| Score not resetting after choosing to play again | I overlooked that the player could choose to play again from the main menu after thir first game, I just had to add a line of code to rest score to zero when play option is selected |


[Back to Top](<#table-of-content>)
## Deployment
### Heroku

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
1. Log in to your account at heroku.com.
2. Create a new app, add a unique app name and choose your region.
3. Click on create app.
4. Go to "Settings".
5. Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to buid your app from.
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

[Back to Top](<#table-of-content>)
## Credits


### Media
- [Flaticon](https://www.flaticon.com/free-icon/physics_4270905?term=nuclear&page=1&position=16&page=1&position=16&related_id=4270905&origin=search): Nuclear icons created by Freepik - Flaticon</a>
- [Background image](https://www.freepik.com/vectors/fluffy-clouds) 
created by pch.vector - www.freepik.com</a>

### Code
- [Gspread](https://docs.gspread.org/en/v5.4.0/)
- [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) by [https://patorjk.com/](https://patorjk.com/)

## Acknowledgements

### Special thanks to the following:
- Code Institute for providing this learning platform.
- My Mentor, Mo Shami for the valuable guidance and advice.
- CI Slack Community for assistance in any help or queries asked.

[Back to Top](<#table-of-content>)