# Higher Lower Game

The "Higher Lower Game" is a simple command-line-based game where players compare the number of followers of two social media profiles and guess which one has more followers. The game continues until the player makes an incorrect guess.

## Features

- **User Interface**: The game provides a basic text-based user interface.
- **Random Data**: It randomly selects and presents two social media profiles from a list with descriptions, names, and follower counts.
- **Score Tracking**: The player's score is tracked and updated after each correct guess.
- **Game Over**: The game ends when the player makes an incorrect guess, and the final score is displayed.

## Usage

1. Run the game by executing the Python script in your terminal:
   python higher_lower_game.py

2. You will be presented with two social media profiles and prompted to guess which one has more followers by typing 'A' or 'B'.

3. If your guess is correct, your score will increase, and the game will continue with a new comparison. If you make an incorrect guess, the game ends, and your final score is displayed.

4. To play again, you can re-run the script.

## Dependencies

- The game uses the `art` library to display the game logo and "vs" symbol.
- It also imports data from the `game_data` module, which includes social media profiles.

## Acknowledgments

This project is inspired by the "Higher or Lower" type of game and serves as a fun and simple text-based game example. You can expand upon it, add more profiles, and customize it to create your own version of the game.

Feel free to modify and expand upon this README to suit your specific project requirements and audience.
