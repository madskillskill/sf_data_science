# Project #1. Guessing game

## Contents
* [Preface](https://github.com/madskillskill/sf_data_science/blob/main/Project%20%231/README.md#Preface)
* [Files](https://github.com/madskillskill/sf_data_science/tree/main/Project%20%231#Files)
* [Results](https://github.com/madskillskill/sf_data_science/tree/main/Project%20%231#Results)
## Preface
I've started to use VS Code, Github and Jupyter while learning to code in Python. These little games show how proficient I'm at it.
## Files
* [**game.py**](https://github.com/madskillskill/sf_data_science/blob/main/Project%20%231/game.py) is a prototype of guessing game where a human user is invited to pick the right number in the least amount of tries. The games tips the player if they picked a number too small or too big;
* [**game_v2.py**](https://github.com/madskillskill/sf_data_science/blob/main/Project%20%231/game_v2.py) is where the program itself plays this game 1000 times, but its' guesses are random and it doesn't adjust its' strategy in any way, so it need ~100 guesses on average;
* [**game_v3.py**]() provides a modified guessing mechanism. It defines the range of possible answers first, and then picks the number right in the middle, so every step divides the amount of possible answers in two. At most, it needs only 7 tries to win, and the average result in 1000 games sits at lovely 4.9 guesses.
* [**game.ipynb**](https://github.com/madskillskill/sf_data_science/blob/main/Project%20%231/game.ipynb) is a presentation-ready showcase of all three of them, but be warned – player's input doesn't work there well so the first game is better run as it's own file;
* [**readme.md**](https://github.com/madskillskill/sf_data_science/blob/main/Project%20%231/README.md) is the very thing you are reading right now.
* [**requirements.exe**]() makes sure you'd be able to run it as the time passes. I used Python 3.10.4 64-bit.
## Results
It was fun to build this game and make it play with itself, making it more and more effective. Using new tools was great too: Git tech is very handy and Jupyter looks neat and easy to use.