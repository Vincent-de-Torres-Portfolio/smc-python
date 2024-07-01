"""
Vincent de Torres
CS87A-Summer 2024

This script calculates the double and quadruple of a given number and prints the results in a formatted string.

Functions:
- up_it(number): Calculate the double and quadruple of a number and return a formatted string.
- main(): Main function to prompt user input for a number, calculate results using up_it function,
          and then iterate through numbers 1 to 10 to display their results.

"""

def up_it(number):
    """
    Calculate the double and quadruple of a given number and return a formatted string.
    
    Args:
    - number (int): The number to perform calculations on.
    
    Returns:
    - str: Formatted string containing the double and quadruple of the input number.
    """
    double_up = number * 2
    quadruple_up = number * 4
    return f"\\~Double up is {double_up}~\\-----/~Quadruple up is {quadruple_up}~/"

def main():
    """
    Main function to prompt user input for a number, calculate results using up_it function,
    and then iterate through numbers 1 to 10 to display their results.
    """
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program : \n")
            break

        try:
            number = int(user_input)
            result = up_it(number)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Challenge: Loop for numbers 1 through 10
    for number in range(1, 11):
        result = up_it(number)
        print(result)

if __name__ == "__main__":
    main()
