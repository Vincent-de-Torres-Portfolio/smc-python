
"""
Vincent de Torres
CS87A-Summer 2024
Filename: guessing_game.py

This module simulates a guessing game where the player and the dealer (program) each guess a number. The goal is to be closest to the target number without going over. The player and dealer are randomly assigned colors (blue or yellow) for each game, and the banner theme color is based on who is leading.

Constants:
- DEFAULT_TARGET (int): The default target number to be guessed.
- LOWER_BOUND (int): The lower bound for guesses.
- UPPER_BOUND (int): The upper bound for guesses.

Functions:
- clear_screen(): Clears the terminal screen.
- print_message(message, color=ANSI_RESET): Prints a message with a border and optional color.
- welcome_message(): Displays the welcome message for the game.
- get_player_guess(): Prompts the player to enter a guess within the specified bounds.
- generate_dealer_guess(): Generates a random guess for the dealer.
- calculate_difference(target, guess): Calculates the difference between the target and a guess.
- determine_winner(player_guess, dealer_guess, target): Determines the winner based on the closest guess to the target.
- print_game_details(target, player_guess, player_difference, dealer_guess, dealer_difference, result, round_type, color): Prints the details of the game round.
- generate_target_number(): Generates a random target number between the lower and upper bounds.
- play_again(): Prompts the player to decide whether to play another round.
- print_lead(player_points, dealer_points, player_color, dealer_color): Prints the current lead based on points and returns the leading color.
- input_processor(): Processes the game logic, manages rounds, and tracks scores.
- main(): Executes the main game flow.
"""

import random
import os

DEFAULT_TARGET = 21
LOWER_BOUND = 0
UPPER_BOUND = 100

ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_BRIGHT_GREEN = "\033[92m"
ANSI_BLUE = "\033[34m"
ANSI_YELLOW = "\033[33m"
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"


def clear_screen():
    os.system('clear')

def print_message(message, color=ANSI_RESET):
    def print_border(width=90,color=ANSI_RESET):
        print(f"{color}{'▂' * width}{ANSI_RESET}")
    def print_message(message, width=90, align='center'):
        if align == 'center':
            print(f"{color}{ANSI_BOLD}{message.center(width)}{ANSI_RESET}")
        elif align == 'left':
            print(f"{color}{message.ljust(width)}{ANSI_RESET}")
        elif align == 'right':
            print(f"{color}{message.rjust(width)}{ANSI_RESET}")
    def print_empty_line():
        print()
    
    print_empty_line()
    print_message(message, align='center')
    print_border(color=ANSI_YELLOW)

def welcome_message():
    clear_screen()
    print_message("Welcome to the Guessing Game!", ANSI_BLUE)
    print("The goal is to be closest to the target number.")
    print()

def get_player_guess():
    while True:
        try:
            guess = int(input("Player, please pick a number between 0 and 100: "))
            if LOWER_BOUND <= guess <= UPPER_BOUND:
                return guess
            else:
                print_message("Please enter a number between 0 and 100.", ANSI_RED)
        except ValueError:
            print_message("Invalid input. Please enter a number.", ANSI_RED)

def generate_dealer_guess():
    return random.randint(LOWER_BOUND, UPPER_BOUND)

def calculate_difference(target, guess):
    return abs(target - guess)

def determine_winner(player_guess, dealer_guess, target):
    player_difference = calculate_difference(target, player_guess)
    dealer_difference = calculate_difference(target, dealer_guess)
    
    if player_difference < dealer_difference:
        result = "Player wins"
    elif dealer_difference < player_difference:
        result = "Dealer wins"
    else:
        result = "It's a tie"
    
    return result, player_difference, dealer_difference

def print_game_details(target, player_guess, player_difference, dealer_guess, dealer_difference, result, round_type, color):
    print(f"{'Round type':<20} : {round_type}")
    print(f"{'Target number':<20} : {target}")
    print(f"{'Player\'s guess':<20} : {player_guess}")
    print(f"{'Player\'s difference':<20} : {player_difference}")
    print(f"{'Dealer\'s guess':<20} : {dealer_guess}")
    print(f"{'Dealer\'s difference':<20} : {dealer_difference}")
    print(f"{'Result':<20} : {result}")
    print()

def generate_target_number():
    """Generate a random target number between 0 and 100."""
    return random.randint(LOWER_BOUND, UPPER_BOUND)

 

def print_lead(player_points, dealer_points, player_color, dealer_color):
    lead_color = player_color if player_points > dealer_points else dealer_color
    player_score_color = ANSI_BRIGHT_GREEN if player_points > dealer_points else ANSI_RED
    dealer_score_color = ANSI_BRIGHT_GREEN if dealer_points > player_points else ANSI_RED
    
    print(f"{player_score_color}PLAYER: {player_points}{ANSI_RESET}   {dealer_score_color}DEALER: {dealer_points}{ANSI_RESET}")
    return lead_color

def input_processor():
    target = DEFAULT_TARGET
    player_color = random.choice([ANSI_BLUE, ANSI_YELLOW])
    dealer_color = ANSI_YELLOW if player_color == ANSI_BLUE else ANSI_BLUE
    
    round_type = "Default Mode"
    welcome_message()
    
    player_guess = get_player_guess()
    dealer_guess = generate_dealer_guess()
    
    result, player_difference, dealer_difference = determine_winner(player_guess, dealer_guess, target)
    
    if result == "Player wins":
        player_points = 1
        dealer_points = 0
    elif result == "Dealer wins":
        player_points = 0
        dealer_points = 1
    else:
        player_points = 0
        dealer_points = 0
    
    print_game_details(target, player_guess, player_difference, dealer_guess, dealer_difference, result, round_type, player_color)
    
    lead_color = print_lead(player_points, dealer_points, player_color, dealer_color)
    
    

    print_message("Thank you for playing!", lead_color)
    print(f"{'Final Score':<20}")
    print_lead(player_points, dealer_points, player_color, dealer_color)

def main():
    input_processor()

if __name__ == "__main__":
    main()
