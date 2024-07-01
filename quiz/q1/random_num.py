"""
Vincent de Torres
CS87A-Summer 2024 
Filename: random.py

Problem #4: Random

Print out a random number between 5 and 8 using the random function.
Show two different ways:
1. Inclusive of 8.
2. Non-inclusive of 8.

Example:
- Output (inclusive of 8): 7
- Output (non-inclusive of 8): 5
"""

import random

def print_task():
    print("""
    Print out a random number between 5 and 8 using the random function.
    Show two different ways:
    1. Inclusive of 8.
    2. Non-inclusive of 8.
    
    Example:
    - Output (inclusive of 8): 7
    - Output (non-inclusive of 8): 5
    """)

def generate_random_inclusive():
    """
    Generates a random number inclusive of 8 between 5 and 8.
    """
    random_num_inclusive = random.randint(5, 8)
    print(f"| {'Random number (inclusive of 8)':>40} | {random_num_inclusive:>3} |")

def generate_random_non_inclusive():
    """
    Generates a random number non-inclusive of 8 between 5 and 7.
    """
    random_num_non_inclusive = random.randint(5, 7)
    print(f"| {'Random number (non-inclusive of 8)':>40} | {random_num_non_inclusive:>3} |")

def main():
    print_task()
    generate_random_inclusive()
    print()
    generate_random_non_inclusive()

if __name__ == "__main__":
    main()

