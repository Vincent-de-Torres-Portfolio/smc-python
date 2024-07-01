"""
Vincent de Torres
CS87A-Summer 2024

Functions:
- print_initials(): Prints a decorative initials pattern.
- modify_grid(grid, color): Modifies the grid by replacing characters and adding color escape sequences.
- animate(grid, colors): Animates the grid with changing colors.
- combine_lines(grid, colors): Combines each line in the grid with all color variations into a single line.
- clear(): Clears the terminal screen
"""
import time,os
def print_initials():
    print("\n")

    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄-𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄      𐌖𐌉𐌍𐌂𐌄 ")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄  \t  𐌖𐌉𐌍𐌂𐌄      𐌖𐌉𐌍𐌂𐌄   ")
    print("\t   𐌖𐌉𐌍𐌂𐌄 𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄 ")
    print("\t      𐌖𐌉𐌍 𐌖𐌉𐌍  \t\t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄  ")
    print("\t        𐌖𐌍𐌂𐌄   \t\t   𐌖𐌉𐌍𐌂-𐌖𐌖𐌍𐌂  \n")

def modify_grid(grid, color):
    """
    Modify the grid by replacing characters and adding color escape sequences.

    Parameters:
    - grid (list of str): List containing strings representing each line of the grid.
    - color (str): ANSI escape sequence for color.

    Returns:
    - list of str: Modified grid with characters replaced and colored.
    """
    modified_grid = []
    for line in grid:
        modified_line = ''
        for char in line:
            if char == '█':
                modified_line += f"{color} \033[0m"
            elif char == '░':
                modified_line += f"{color}█\033[0m"
            elif char == '▒▒':
                modified_line += f"{color}▒▒\033[0m"
            else:
                modified_line += char
        modified_grid.append(modified_line)
    return modified_grid

def animate(grid,colors):
    # Animation loop
    for color in colors:
        modified_grid = modify_grid(grid, color)
        for offset in range(10):
            clear()

            if offset % 2 == 1:
                print('')
            elif offset % 3 == 2:
                print('')
                print('')

            for line in modified_grid:
                print(f'\t' * offset + line)
            time.sleep(0.3)
def combine_lines(grid, colors):
    """
    Combine each line in the grid with all color variations into a single line.

    Parameters:
    - grid (list of str): List containing strings representing each line of the grid.
    - colors (list of str): List of ANSI escape sequences for colors.

    Returns:
    - list of str: Combined grid variations with characters replaced and colored.
    """
    combined_grid = []
    for line in grid:
        combined_line = ''
        for color in colors:
            modified_line = modify_grid([line], color)[0]  # Apply color modification to the line
            combined_line += modified_line  # Concatenate modified line
        combined_grid.append(combined_line)
    return combined_grid

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    grid = [
        "                   ░░ ░░ ░░                   ",
        "             ░░ ░░ ░░ ░░ ░░ ░░ ░░             ",
        "          ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░          ",
        "          ░░ ░█ ██ █░ ░░ ░░ ░░ ░█ ██ █░       ",
        "       ░░ ░░ ██ ██ ▒▒ ░░ ░░ ░░ ██ ██ ▒▒       ",
        "       ░░ ░░ ██ ██ █░ ░░ ░░ ░░ ██ ██ █░       ",
        "       ░░ ░░ ░█ ██ █░ ░░ ░░ ░░ ░█ ██ █░       ",
        "       ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░       ",
        "       ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░       ",
        "       ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░       ",
        "       ░░ ░░ ░░    ░░ ░░ ░░    ░░ ░░ ░░       ",
        "        ░ ░░ ░      ░ ░░ ░      ░ ░░ ░        ",
        "          ░░          ░░          ░░          ",
    ]


    colors = [
        '\033[95m',   # Pink
        '\033[38;5;208m',  # Orange
        '\033[91m',   # Red
        '\033[96m'    # Cyan
    ]

    print_initials()



    # combined_grid = combine_lines(grid, colors)
    # for line in combined_grid:
    #     print(line)

    animate(grid,colors)
