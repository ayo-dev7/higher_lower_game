from art import logo, vs
from game_data import data
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def play_game():
    score = 0
    print(logo)

    while True:
        option_a = random.choice(data)
        option_b = random.choice(data)

        while option_a == option_b:
            option_b = random.choice(data)

        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(vs)
        print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (user_choice == 'a' and option_a['follower_count'] > option_b['follower_count']) or \
           (user_choice == 'b' and option_b['follower_count'] > option_a['follower_count']):
            score += 1
            clear_screen()
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

play_game()
