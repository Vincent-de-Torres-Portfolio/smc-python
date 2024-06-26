"""
filename: hello_world.py
gist    : https://gist.github.com/devinci-it/522d42a1cbd29da4665147a153d5d7d3#file-hello_world-py

This script demonstrates printing "HELLO WORLD!" with styled formatting using ANSI escape codes.

Vincent de Torres
CS87A-Summer 2024 | Check-In Homework

"""


def hello():
    """
    Prints "HELLO WORLD!" with styled formatting.
    - "HELLO" is printed in blue color.
    - "WORLD!" is printed in yellow color.
    """

    blue_color = "\033[1;34m"
    color_reset = '\033[0m'
    color_yellow = '\033[93m'

    # Print a line of yellow dashes
    print(f"{color_yellow}{'▂' * 80}{color_reset}")

    # Text to format
    text = "HELLO WORLD!"
    # Print formatted text with blue "HELLO" and yellow "WORLD!"
    print(f"\n\t{blue_color}{text.split(' ')[0]}{color_yellow}  {text.split(' ')[1]}{color_reset}")

    # Print another line of yellow dashes
    print(f"{blue_color}{'▂' * 80}{color_reset}")


if __name__ == "__main__":
    hello()
