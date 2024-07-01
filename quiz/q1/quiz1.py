"""
Quiz #1 Solutions

This script contains solutions to the problems outlined in Quiz #1:
1. Print name ten times using different loop styles.
2. Check if a number is greater than 50.
3. Print absolute value of a number.
4. Generate a random number between 5 and 8.
5. Demonstrate math functions: square root (standard), exponential (numpy).
6. Categorize voltage levels based on user input.
7. Print name with loop counter.
8. Count numbers greater than 50 until a negative number is entered.

Note: Advanced/optional features like input validation are included where applicable.
"""

import random
import math
import numpy as np

def print_title(title):
    """
    Print a title header.
    """
    print(f"### {title}")

def print_separator():
    """
    Print a separator line.
    """
    print("=" * 40)

# Problem #1: Name
def print_name_ten_times():
    """
    Problem #1: Name
    
    Use a loop to print your name ten times. Show two different loop styles:
    1. Using a for loop.
    2. Using a while loop.
    """
    print_title("Problem #1: Name")
    print("""
    Use a loop to print your name ten times. Show two different loop styles:
    1. Using a for loop.
    2. Using a while loop.
    """)
    print("Using a for loop:")
    for i in range(10):
        print(f"Vincent de Torres #{i}")

    print("\nUsing a while loop:")
    counter = 0
    while counter < 10:
        print(f"Vincent de Torres #{counter}")
        counter += 1

    print_separator()

# Problem #2: Fifty
def check_number_greater_than_50():
    """
    Problem #2: Fifty
    
    Ask the user to enter a number and tell them if the number is greater than 50.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: 45
    - Output: The number is not greater than 50.
    """
    print_title("Problem #2: Fifty")
    print("""
    Ask the user to enter a number and tell them if the number is greater than 50.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: 45
    - Output: The number is not greater than 50.
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num > 50:
            print("The number is greater than 50.")
        else:
            print("The number is not greater than 50.")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #3: Absolute
def print_absolute_value():
    """
    Problem #3: Absolute
    
    Ask the user to enter a number and print its absolute value.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: -10
    - Output: The absolute value of -10 is 10.
    """
    print_title("Problem #3: Absolute")
    print("""
    Ask the user to enter a number and print its absolute value.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: -10
    - Output: The absolute value of -10 is 10.
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        print(f"The absolute value of {num} is {abs(num)}.")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #4: Random
def generate_random_number():
    """
    Problem #4: Random
    
    Print out a random number between 5 and 8 using the random function.
    Show two different ways:
    1. Inclusive of 8.
    2. Non-inclusive of 8.
    
    Example:
    - Output (inclusive of 8): 7
    - Output (non-inclusive of 8): 5
    """
    print_title("Problem #4: Random")
    print("""
    Print out a random number between 5 and 8 using the random function.
    Show two different ways:
    1. Inclusive of 8.
    2. Non-inclusive of 8.
    
    Example:
    - Output (inclusive of 8): 7
    - Output (non-inclusive of 8): 5
    """)
    print("Inclusive of 8:")
    random_num_inclusive = random.randint(5, 8)
    print(f"Random number (inclusive of 8): {random_num_inclusive}")

    print("\nNon-inclusive of 8:")
    random_num_non_inclusive = random.randint(5, 7)
    print(f"Random number (non-inclusive of 8): {random_num_non_inclusive}")

    print_separator()

# Problem #5: Free Choice
def demonstrate_math_functions():
    """
    Problem #5: Free Choice
    
    Write a program that uses a math function not used before (e.g., power, square root).
    Show two different examples:
    1. Using standard Python math functions.
    2. Using numpy math functions.
    
    Example (using standard math):
    - Calculate the square root of a number.
    
    Example (using numpy):
    - Calculate the exponential of a number.
    """
    print_title("Problem #5: Free Choice")
    print("""
    Write a program that uses a math function not used before (e.g., power, square root).
    Show two different examples:
    1. Using standard Python math functions.
    2. Using numpy math functions.
    
    Example (using standard math):
    - Calculate the square root of a number.
    
    Example (using numpy):
    - Calculate the exponential of a number.
    """)
    # Using standard math module
    num = 16
    sqrt_num = math.sqrt(num)
    print(f"\nUsing standard math:")
    print(f"Square root of {num} is {sqrt_num}")

    # Using numpy module
    num = 2
    exp_num = np.exp(num)
    print(f"\nUsing numpy:")
    print(f"Exponential of {num} is {exp_num}")

    print_separator()

# Problem #6: Voltage
def classify_voltage():
    """
    Problem #6: Voltage
    
    Ask the user to enter a number and categorize it based on voltage levels:
    - <= 30: Low voltage
    - 31-59: Medium voltage
    - 60-239: High voltage
    - >= 240: Electrocution
    
    Example:
    - Input: 45
    - Output: Medium voltage
    """
    print_title("Problem #6: Voltage")
    print("""
    Ask the user to enter a number and categorize it based on voltage levels:
    - <= 30: Low voltage
    - 31-59: Medium voltage
    - 60-239: High voltage
    - >= 240: Electrocution
    
    Example:
    - Input: 45
    - Output: Medium voltage
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num <= 30:
            print("Low voltage.")
        elif 31 <= num <= 59:
            print("Medium voltage.")
        elif 60 <= num < 240:
            print("High voltage.")
        elif num >= 240:
            print("Electrocution!")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #7: Namecount
def print_name_with_counter():
    """
    Problem #7: Namecount
    
    Redo Problem #1 but also print the value of the loop counter alongside the name.
    
    Example:
    - Output: Patti Koenig #0
              Patti Koenig #1
              Patti Koenig #2
    """
    print_title("Problem #7: Namecount")
    print("""
    Redo Problem #1 but also print the value of the loop counter alongside the name.
    
    Example:
    - Output: Patti Koenig #0
              Patti Koenig #1
              Patti Koenig #2
    """)
    print("Using a for loop:")
    for i in range(5):
        print(f"Vincent de Torres #{i}")

    print("\nUsing a while loop:")
    counter = 0
    while counter < 5:
        print(f"Vincent de Torres #{counter}")
        counter += 1

    print_separator()

# Problem #8: Fiftytally
def count_numbers_greater_than_50():
    """
    Problem #8: Fiftytally
    
    Redo Problem #2 but put it in a loop that continues until a negative number is entered.
    Count and display how many numbers entered are greater than 50.
    
    Example:
    - Input: 60, 45, 55, -5
    - Output: You entered 3 numbers greater than 50.
    """
    print_title("Problem #8: Fiftytally")
    print("""
    Redo Problem #2 but put it in a loop that continues until a negative number is entered.
    Count and display how many numbers entered are greater than 50.
    
    Example:
    - Input: 60, 45, 55, -5
    - Output: You entered 3 numbers greater than 50.
    """)
    count_over_50 = 0
    while True:
        num = input("Enter a number (enter a negative number to exit): ")
        if num.isdigit():
            num = int(num)
            if num < 0:
                break
            if num > 50:
                count_over_50 += 1
        else:
            print("Invalid input. Please enter a valid number.")

    print(f"You entered {count_over_50} numbers greater than 50.")

    print_separator()

# Main function to run all solutions
def main():
    print_name_ten_times()
    check_number_greater_than_50()
    print_absolute_value()
    generate_random_number()
    demonstrate_math_functions()
    classify_voltage()
    print_name_with_counter()
    count_numbers_greater_than_50()

if __name__ == "__main__":
    main()
"""
Quiz #1 Solutions

This script contains solutions to the problems outlined in Quiz #1:
1. Print name ten times using different loop styles.
2. Check if a number is greater than 50.
3. Print absolute value of a number.
4. Generate a random number between 5 and 8.
5. Demonstrate math functions: square root (standard), exponential (numpy).
6. Categorize voltage levels based on user input.
7. Print name with loop counter.
8. Count numbers greater than 50 until a negative number is entered.

Note: Advanced/optional features like input validation are included where applicable.
"""

import random
import math
import numpy as np

def print_title(title):
    """
    Print a title header.
    """
    print(f"### {title}")

def print_separator():
    """
    Print a separator line.
    """
    print("=" * 40)

# Problem #1: Name
def print_name_ten_times():
    """
    Problem #1: Name
    
    Use a loop to print your name ten times. Show two different loop styles:
    1. Using a for loop.
    2. Using a while loop.
    """
    print_title("Problem #1: Name")
    print("""
    Use a loop to print your name ten times. Show two different loop styles:
    1. Using a for loop.
    2. Using a while loop.
    """)
    print("Using a for loop:")
    for i in range(10):
        print(f"Vincent de Torres #{i}")

    print("\nUsing a while loop:")
    counter = 0
    while counter < 10:
        print(f"Vincent de Torres #{counter}")
        counter += 1

    print_separator()

# Problem #2: Fifty
def check_number_greater_than_50():
    """
    Problem #2: Fifty
    
    Ask the user to enter a number and tell them if the number is greater than 50.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: 45
    - Output: The number is not greater than 50.
    """
    print_title("Problem #2: Fifty")
    print("""
    Ask the user to enter a number and tell them if the number is greater than 50.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: 45
    - Output: The number is not greater than 50.
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num > 50:
            print("The number is greater than 50.")
        else:
            print("The number is not greater than 50.")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #3: Absolute
def print_absolute_value():
    """
    Problem #3: Absolute
    
    Ask the user to enter a number and print its absolute value.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: -10
    - Output: The absolute value of -10 is 10.
    """
    print_title("Problem #3: Absolute")
    print("""
    Ask the user to enter a number and print its absolute value.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: -10
    - Output: The absolute value of -10 is 10.
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        print(f"The absolute value of {num} is {abs(num)}.")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #4: Random
def generate_random_number():
    """
    Problem #4: Random
    
    Print out a random number between 5 and 8 using the random function.
    Show two different ways:
    1. Inclusive of 8.
    2. Non-inclusive of 8.
    
    Example:
    - Output (inclusive of 8): 7
    - Output (non-inclusive of 8): 5
    """
    print_title("Problem #4: Random")
    print("""
    Print out a random number between 5 and 8 using the random function.
    Show two different ways:
    1. Inclusive of 8.
    2. Non-inclusive of 8.
    
    Example:
    - Output (inclusive of 8): 7
    - Output (non-inclusive of 8): 5
    """)
    print("Inclusive of 8:")
    random_num_inclusive = random.randint(5, 8)
    print(f"Random number (inclusive of 8): {random_num_inclusive}")

    print("\nNon-inclusive of 8:")
    random_num_non_inclusive = random.randint(5, 7)
    print(f"Random number (non-inclusive of 8): {random_num_non_inclusive}")

    print_separator()

# Problem #5: Free Choice
def demonstrate_math_functions():
    """
    Problem #5: Free Choice
    
    Write a program that uses a math function not used before (e.g., power, square root).
    Show two different examples:
    1. Using standard Python math functions.
    2. Using numpy math functions.
    
    Example (using standard math):
    - Calculate the square root of a number.
    
    Example (using numpy):
    - Calculate the exponential of a number.
    """
    print_title("Problem #5: Free Choice")
    print("""
    Write a program that uses a math function not used before (e.g., power, square root).
    Show two different examples:
    1. Using standard Python math functions.
    2. Using numpy math functions.
    
    Example (using standard math):
    - Calculate the square root of a number.
    
    Example (using numpy):
    - Calculate the exponential of a number.
    """)
    # Using standard math module
    num = 16
    sqrt_num = math.sqrt(num)
    print(f"\nUsing standard math:")
    print(f"Square root of {num} is {sqrt_num}")

    # Using numpy module
    num = 2
    exp_num = np.exp(num)
    print(f"\nUsing numpy:")
    print(f"Exponential of {num} is {exp_num}")

    print_separator()

# Problem #6: Voltage
def classify_voltage():
    """
    Problem #6: Voltage
    
    Ask the user to enter a number and categorize it based on voltage levels:
    - <= 30: Low voltage
    - 31-59: Medium voltage
    - 60-239: High voltage
    - >= 240: Electrocution
    
    Example:
    - Input: 45
    - Output: Medium voltage
    """
    print_title("Problem #6: Voltage")
    print("""
    Ask the user to enter a number and categorize it based on voltage levels:
    - <= 30: Low voltage
    - 31-59: Medium voltage
    - 60-239: High voltage
    - >= 240: Electrocution
    
    Example:
    - Input: 45
    - Output: Medium voltage
    """)
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num <= 30:
            print("Low voltage.")
        elif 31 <= num <= 59:
            print("Medium voltage.")
        elif 60 <= num < 240:
            print("High voltage.")
        elif num >= 240:
            print("Electrocution!")
    else:
        print("Invalid input. Please enter a valid number.")

    print_separator()

# Problem #7: Namecount
def print_name_with_counter():
    """
    Problem #7: Namecount
    
    Redo Problem #1 but also print the value of the loop counter alongside the name.
    
    Example:
    - Output: Patti Koenig #0
              Patti Koenig #1
              Patti Koenig #2
    """
    print_title("Problem #7: Namecount")
    print("""
    Redo Problem #1 but also print the value of the loop counter alongside the name.
    
    Example:
    - Output: Patti Koenig #0
              Patti Koenig #1
              Patti Koenig #2
    """)
    print("Using a for loop:")
    for i in range(5):
        print(f"Vincent de Torres #{i}")

    print("\nUsing a while loop:")
    counter = 0
    while counter < 5:
        print(f"Vincent de Torres #{counter}")
        counter += 1

    print_separator()

# Problem #8: Fiftytally
def count_numbers_greater_than_50():
    """
    Problem #8: Fiftytally
    
    Redo Problem #2 but put it in a loop that continues until a negative number is entered.
    Count and display how many numbers entered are greater than 50.
    
    Example:
    - Input: 60, 45, 55, -5
    - Output: You entered 3 numbers greater than 50.
    """
    print_title("Problem #8: Fiftytally")
    print("""
    Redo Problem #2 but put it in a loop that continues until a negative number is entered.
    Count and display how many numbers entered are greater than 50.
    
    Example:
    - Input: 60, 45, 55, -5
    - Output: You entered 3 numbers greater than 50.
    """)
    count_over_50 = 0
    while True:
        num = input("Enter a number (enter a negative number to exit): ")
        if num.isdigit():
            num = int(num)
            if num < 0:
                break
            if num > 50:
                count_over_50 += 1
        else:
            print("Invalid input. Please enter a valid number.")

    print(f"You entered {count_over_50} numbers greater than 50.")

    print_separator()

# Main function to run all solutions
def main():
    print_name_ten_times()
    check_number_greater_than_50()
    print_absolute_value()
    generate_random_number()
    demonstrate_math_functions()
    classify_voltage()
    print_name_with_counter()
    count_numbers_greater_than_50()

if __name__ == "__main__":
    main()

