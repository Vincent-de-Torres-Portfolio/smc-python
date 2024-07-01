"""
Vincent de Torres
CS87A-Summer 2024 
Filename: ticket_discount.py

This module simulates a ticket pricing system based on user age.
Users are prompted to enter their age, and based on the age:
- Minors (under 18) get a discounted ticket.
- Senior citizens (65 and older) get a discounted ticket.
- Others pay the full ticket price.

Constants:
- TICKET_COST (int): The standard ticket cost.
- MINOR_DISCOUNT (int): Discounted price for minors.
- SENIOR_DISCOUNT (int): Discounted price for seniors.
- MINOR_AGE_THRESHOLD (int): Age threshold for minors.
- SENIOR_AGE_THRESHOLD (int): Age threshold for seniors.

Functions:
- print_message(message): Prints a message in a banner-like ASCII art style.
- get_user_age(): Prompts the user to enter their age and returns it.
- calculate_ticket_price(age): Calculates the ticket price based on age.
- format_money(amount): Formats an amount as a monetary value with two decimal places.
- display_ticket_info(age, ticket_price): Displays ticket price information based on age.
- main(): Executes the main logic of the ticket pricing system.

"""

import datetime

# Constants for ticket pricing
TICKET_COST = 14
MINOR_DISCOUNT = 10
SENIOR_DISCOUNT = 10

MINOR_AGE_THRESHOLD = 18
SENIOR_AGE_THRESHOLD = 65

def print_message(message):
    """
    Prints a message in a banner-like ASCII art style using box-drawing characters.

    Parameters:
    - message (str): The message to be displayed.
    """
    border_top = '┌' + '─' * (90 + 2) + '┐'
    border_bottom = '└' + '─' * (90 + 2) + '┘'
    print(border_top)
    print(f'\t{message} ')
    print(border_bottom)

def get_user_age():
    """
    Prompt the user to enter their age and return it as an integer.
    """
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Please enter a valid age (a number).")

def calculate_ticket_price(age):
    """
    Calculate the ticket price based on the user's age.
    Returns the calculated ticket price as an integer.
    """
    if age < MINOR_AGE_THRESHOLD:
        return MINOR_DISCOUNT
    elif age >= SENIOR_AGE_THRESHOLD:
        return SENIOR_DISCOUNT
    else:
        return TICKET_COST

def format_money(amount):
    """
    Format the given amount as a monetary value with dollar sign and two decimal places.
    """
    return f"${amount:.2f}"

def display_ticket_info(age, ticket_price):
    """
    Display information about the ticket price based on the user's age.
    """
    if age < MINOR_AGE_THRESHOLD:
        print_message(f"As you are a minor (under {MINOR_AGE_THRESHOLD}), your ticket price is {format_money(ticket_price)}.")
    elif age >= SENIOR_AGE_THRESHOLD:
        print_message(f"As you are a senior citizen (Age  {SENIOR_AGE_THRESHOLD} and above), your ticket price is {format_money(ticket_price)}.")
    else:
        print_message(f"Purchasing ticket at full price {format_money(ticket_price)}.")

def main():
    """
    Main function to simulate the ticket pricing scenario.
    """
    print_message("Welcome to Ticket Pricing System")
    print(f"Tickets cost {format_money(TICKET_COST)}.")
    age = get_user_age()
    ticket_price = calculate_ticket_price(age)
    display_ticket_info(age, ticket_price)
 
# Execute the main function
if __name__ == "__main__":
    main()
