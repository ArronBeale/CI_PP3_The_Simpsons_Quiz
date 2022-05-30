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
   3. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
   1. [Flowcharts](#flowcharts)
   2. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
   1. [Languages](#Languages)
   2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
   1. [PEP8 Validation](#pep8-validation)
   4. [Performance](#performance)
   5. [Device Testing](#Performing-tests-on-devices)
   6. [Browser Compatability](#browser-compatability)
   7. [Testing User Stories](#testing-user-stories)
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

### User Stories

### First Time User
1. As a player, I would like to know how to play
2. As a player, I would like to have a main menu
3. As a player, I would like to register my name and email for future visits
4. As a player, I would like to upload my score to a scoreboard
5. As a player, I would like to know how to play

### Returning User
6. As a returning player, I would like to be remembered
7. As a returning player, I would like to view a scoreboard
 
### Site Owner
8. As the site owner, I would like the game to be challenging and fun.
13. As the site owner, I would like an eye catching logo
14. As the site owner, I would like some humor on the main menu
15. As the site owner, I would like valid data from the player especially correct email formats
16. As the site owner, I would like a database of player scores, names and emails
17. As the site owner, i would like to give the option for a player to submit their score or not
 
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
- 
- 
- User stories covered:
<details><summary>Quiz image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_quiz.PNG">
</details>

### Validate New Player
- 
- 
- User stories covered:
<details><summary>Validate New Player Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_new_player.PNG">
</details>

### Validate returning Player
- 
- 
- User stories covered:
<details><summary>Validate returning Player Image
</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_returning_player.PNG">
</details>

### Validate and Greet Name
- 
- 
- User stories covered:
<details><summary>Validate and Greet Name Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_validate_greet_name.PNG">
</details>

### Main Menu
- 
- 
- User stories covered:
<details><summary>Main Menu Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu2.PNG">
</details>

### Logo
- 
- 
- User stories covered:
<details><summary>Logo Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_main_menu.PNG">
</details>

### How to Play
- 
- 
- User stories covered:
<details><summary>User stories covered</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_how_to_play.PNG">
</details>

### Scoreboard
- 
- 
- User stories covered:
<details><summary>Scoreboard Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_scoreboard.PNG">
</details>

### Add to Scoreboard
- 
- 
- User stories covered:
<details><summary>Add to Scoreboard Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_add_to_scoreboard.PNG">
</details>

### Player Database
- 
- 
- User stories covered:
<details><summary>Players Database Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_player_database.PNG">
</details>

### Scoreboard Database
- 
- 
- User stories covered:
<details><summary>Scoreboard Database Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_scoreboard_database.PNG">
</details>

### Results
- 
- 
- User stories covered:
<details><summary>Results Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_results.PNG">
</details>

### Stats
- 
- 
- User stories covered:
<details><summary>Stats Image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_stats.PNG">
</details>

[Back to Top](<#table-of-content>)
## Validation


### PEP8 Validation
<details><summary>Home</summary>
<img src="">
</details>


### Testing User Stories
First Time User:
1. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| | | |  |
| | | | |

<details><summary>Images</summary>
<img src="">
<img src="">
</details>

[Back to Top](<#table-of-content>)
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| | |


[Back to Top](<#table-of-content>)
## Deployment
The website was deployed to GitHub Pages via the following:
1. From Github repository select settings
2. Select pages from the left menu
3. Select the master branch
4. When the page refreshes you will see a message to notify you the site is now published

You can for fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

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
- Favicon: <a href="https://www.flaticon.com/free-icons/nuclear" title="nuclear icons">Nuclear icons created by Freepik - Flaticon</a>
- Background image: <a href="https://www.freepik.com/vectors/fluffy-clouds">Fluffy clouds vector created by pch.vector - www.freepik.com</a>

### Code
- 

## Acknowledgements

Special thanks to the following:
- 

[Back to Top](<#table-of-content>)