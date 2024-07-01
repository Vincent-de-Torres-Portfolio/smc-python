"""
Vincent de Torres
CS87A-Summer 2024 
Filename: fifty.py

Problem #2 and #8: Fifty and Count Greater than 50

Ask the user to enter numbers and tell them if each number is greater than 50. 
Count how many numbers are greater than 50 until a negative number is entered.

Example:
- Input: 45, 55, 60, 40, -2
- Output:
  - The number 45 is not greater than 50.
  - The number 55 is greater than 50.
  - The number 60 is greater than 50.
  - The number 40 is not greater than 50.
  - You entered 2 numbers greater than 50.
"""

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_task():
    print("""
    Ask the user to enter numbers and tell them if each number is greater than 50. 
    Count how many numbers are greater than 50 until a negative number is entered.
    
    Example:
    - Input: 45, 55, 60, 40, -2
    - Output:
      - The number 45 is not greater than 50.
      - The number 55 is greater than 50.
      - The number 60 is greater than 50.
      - The number 40 is not greater than 50.
      - You entered 2 numbers greater than 50.
    """)

def validate_input(input_str):
    """
    Validates if the input string represents a numeric value.
    
    Parameters:
    - input_str (str): The input string to validate.
    
    Returns:
    - bool: True if the input string is numeric, False otherwise.
    """
    return input_str.lstrip('-').isdigit()

def check_number(num):
    """
    Checks if the provided number is greater than 50.
    
    Parameters:
    - num (int): The number to check.
    
    Returns:
    - bool: True if the number is greater than 50, False otherwise.
    """
    if num > 50:
        return True
    else:
        return False

def main():
    print_task()
    results = [(">","<")]
    while True:
        num_str = input("Enter a number (enter a negative number to exit): ")
        if validate_input(num_str):
            num = int(num_str)
            if num < 0:
                break
            if check_number(num):
                print(f"The number {num} is {GREEN}greater than 50{RESET}.")
                results.append((num, ''))
            else:
                print(f"The number {num} is {RED}not greater than 50{RESET}.")
                results.append(('', num))
        else:
            print("Invalid input. Please enter a valid number.")
    
    count_greater_than_50 = sum(1 for result in results if result[0] != '')
    print(f"\nYou entered {count_greater_than_50} numbers greater than 50.\n")
    
    # Print results in a table-like format
    print("Results:")
    for num1, num2 in results:
        num1_str = f"{GREEN}{num1:<3}{RESET}" if num1 != '' else ''
        num2_str = f"{RED}{num2:<3}{RESET}" if num2 != '' else ''
        print(f"\t{num1_str:<3} \t| {num2_str:<3}\t |")

if __name__ == "__main__":
    main()

