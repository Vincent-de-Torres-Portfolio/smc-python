"""
Vincent de Torres
CS87A-Summer 2024 
Filename: factorial_visualization.py

Problem:
Calculate the factorial of a non-negative integer provided by the user and visualize it as a product sequence.

Example:
- Input: 5
- Output: The factorial of 5 is: 120
         Visual representation:
         5! = 5 x 4 x 3 x 2 x 1
         ----------------------
         = 120

Special Cases:
- 0! = 1 (By definition)
- Factorial is not defined for negative numbers.

References:
- Python math module documentation: https://docs.python.org/3/library/math.html
"""

import math

def get_valid_integer(prompt):
    """
    Prompts the user for an integer input and validates it.
    
    Returns:
    - An integer inputted by the user.
    
    Raises:
    - ValueError: If the input is not a valid integer.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_factorial(num):
    """
    Computes the factorial of a non-negative integer using math.factorial.
    
    Args:
    - num (int): Non-negative integer for which factorial is to be computed.
    
    Returns:
    - Factorial of num.
    
    Raises:
    - ValueError: If num is negative.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(num)

def print_factorial_visualization(num):
    """
    Prints a visual representation of factorial as a product sequence from num! down to 1.
    
    Args:
    - num (int): Non-negative integer for which to calculate and print factorial product sequence.
    """
    print("Visual representation:")
    if num == 0:
        print("0! = 1")  # Special case for 0! which is 1
    else:
        print(f"{num}! = ", end="")
        expression = " x ".join(str(i) for i in range(num, 0, -1))
        print(expression)
        print("-" * len(expression.replace(" ", "")))
        factorial_value = math.factorial(num)
        print(f"= {factorial_value}")

def main():
    """
    Main function to calculate and display factorial of a user-provided integer.
    """
    print("Factorial Calculation")
    
    # Get input value
    num = get_valid_integer("Enter a non-negative integer to calculate its factorial: ")
    
    # Calculate factorial
    try:
        result = get_factorial(num)
        print(f"The factorial of {num} is: {result}")
        
        # Print factorial visual representation
        print_factorial_visualization(num)
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

