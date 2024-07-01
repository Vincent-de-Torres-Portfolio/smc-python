"""
Vincent de Torres
CS87A-Summer 2024 
Filename: ticket_discount.py

Prints two lines of text:
1. 'how low low low ...' with a specified number of iterations using a for loop.
2. 'can you go go go ...' with a specified number of iterations using a while loop.

Constants:
- NUM_ITERATIONS (int): Number of iterations for both lines.

Functions:
- print_low_line(num_iterations): Prints the first line with 'how low' repeated.
- print_go_line(num_iterations): Prints the second line with 'can you go' repeated.
- main(): Executes the program by calling print functions.

Usage:
Run the script to see the output lines printed with the specified number of iterations.
"""

NUM_ITERATIONS = 5  # Number of iterations for both lines

def print_low_line(num_iterations):
    """
    Prints 'how low low low ...' with specified number of iterations.

    Args:
    - num_iterations (int): Number of times to print 'low'.

    """
    print("how", end=" ")
    for _ in range(num_iterations):
        print(f"{'low':<4}", end=" ")
    print()

def print_go_line(num_iterations):
    """
    Prints 'can you go go go ...' with specified number of iterations using a while loop.

    Args:
    - num_iterations (int): Number of times to print 'go'.

    """
    print("can", end=" ")
    count = 0
    while count < num_iterations:
        print(f"{'go':<4}", end=" ")
        count += 1
    print()

def main():
    """
    Main function to execute the program.
    """
    print_low_line(NUM_ITERATIONS)
    print_go_line(NUM_ITERATIONS)

if __name__ == "__main__":
    main()
