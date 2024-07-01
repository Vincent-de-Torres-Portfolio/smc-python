"""
Vincent de Torres
CS87A-Summer 2024 
Filename: absolute.py

Problem #3: Absolute

Ask the user to enter a number and print its absolute value.
Advanced (Optional): Ensure valid input (numeric value).

Example:
- Input: -10
- Output: The absolute value of -10 is 10.
"""

def print_task():
    print("""
    Ask the user to enter a number and print its absolute value.
    Advanced (Optional): Ensure valid input (numeric value).
    
    Example:
    - Input: -10
    - Output: The absolute value of -10 is 10.
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

def main():
    print_task()
    while True:
        num_str = input("Enter a number: ")
        if validate_input(num_str):
            num = int(num_str)
            print(f"The absolute value of {num} is {abs(num)}.")
            break
        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

