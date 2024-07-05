This Python script allows you to play a simple game of blackjack against the computer. It includes functionalities such as dealing cards, calculating scores, checking for blackjack, and determining the winner based on standard blackjack rules.

Requirements
Python 3.x
random module (comes pre-installed with Python)

How to Play
Setup:
Run the script in your Python environment.

Game Start:
You will be prompted to start the game by typing y for yes or n for no.

Gameplay:
You and the computer will each receive two cards initially.
You can choose to get another card (y) or pass (n).
The objective is to get as close to 21 as possible without exceeding it.
Face cards (Jack, Queen, King) are worth 10 points. Aces can be worth 1 or 11 points, whichever is better for the player.

Winning Conditions:
You win if:
You have a higher score than the computer without exceeding 21.
The computer's score exceeds 21 while yours does not.
The computer wins if:
Its score is higher than yours without exceeding 21.
Your score exceeds 21.
Ending the Game:

After each game, you will be asked if you want to play again (y for yes, n for no).
The game will continue until you choose not to play again.
