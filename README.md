# GUESSING GAME

Write a program that generates a random number in the range of 1 through 100, and asks the user to guess what the number is. 
If the user's guess is higher than the randomly generated number, the program should display "Too high, try again." 
If the user's guess is lower, the program prints "Too low, try again." 
If the user guesses the number, the application should congratulate the user and generate a new random number so the game can start over. 
Keep track of the number of guesses a user makes before guessing the correct one and display it with the congratulatory message when the user guesses the number correctly.

Create functions that:</br>
1. generate and return a random number between 1 and 100
2. format and return the failure and congratulatory messages

* Put these function in a module called [helper.py](helper.py) and put the rest of the code in [game.py](game.py). The game module must import the helper module.
