"""
Vincent de Torres
CS87A-Summer 2024 
Filename: print_name.py

Problem #1: Print Name

Use a loop to print your name ten times. Show two different loop styles:
1. Using a for loop.
2. Using a while loop.
"""

NAME = "Vincent de Torres"

def print_task():
    print("""
    Use a loop to print your name ten times. Show two different loop styles:
    1. Using a for loop.
    2. Using a while loop.
    """)

def print_with_for_loop(indexed=True):
    """
    Prints the name using a for loop ten times, with an optional index before the name.
    
    Args:
    - indexed (bool): If True, prints the index before the name. Default is True.
    """
    print("Using a for loop:")
    for i in range(10):
        if indexed:
            print(f"\t{(i+1):<3} {NAME:<20}")
        else:
            print(f"\t{NAME:<20}")

def print_with_while_loop(indexed=True):
    """
    Prints the name using a while loop ten times, with an optional index before the name.
    
    Args:
    - indexed (bool): If True, prints the index before the name. Default is True.
    """
    print("\nUsing a while loop:")
    counter = 0
    while counter < 10:
        if indexed:
            print(f"\t{(counter+1):<3} {NAME:<20}")
        else:
            print(f"\t{NAME:<20}")
        counter += 1

def main():
    print_task()
    
    # Print Task 1 versions without index
    print("\nTask 1: Without Index")
    print_with_for_loop(indexed=False)
    print_with_while_loop(indexed=False)
    
    # Print Task 7 versions with index=True
    print("\nTask 7: With Index")
    print_with_for_loop(indexed=True)
    print_with_while_loop(indexed=True)

if __name__ == "__main__":
    main()

