import os,time

def print_initials():
    print("\n")

    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄-𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄 ")
    print("\t  𐌖𐌉𐌍𐌂𐌄   𐌖𐌉𐌍𐌂𐌄  \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄   ")
    print("\t   𐌖𐌉𐌍𐌂𐌄 𐌖𐌉𐌍𐌂𐌄 \t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄 ")
    print("\t      𐌖𐌉𐌍 𐌖𐌉𐌍  \t\t  𐌖𐌉𐌍𐌂𐌄     𐌖𐌉𐌍𐌂𐌄  ")
    print("\t        𐌖𐌍𐌂𐌄   \t\t   𐌖𐌉𐌍𐌂-𐌖𐌖𐌍𐌂  \n")

def modify_grid(grid, color):
    """
    Modify the grid by replacing characters and adding color escape sequences.

    Parameters:
    - grid (list of str): List containing strings representing each line of the grid.
    - colors (dict): Dictionary containing ANSI escape sequences for colors.

    Returns:
    - list of str: Modified grid with characters replaced and colored.
    """
    modified_grid = []
    for line in grid:
        modified_line = ''
        for char in line:
            if char == '█':
                modified_line += f"{colors[3]} \033[0m"
            elif char == '░':
                modified_line += f"{colors[1]}█\033[0m"
            elif char == '▒▒':
                modified_line += f"{color[3]}▒▒\033[0m"
            else:
                modified_line += char
        modified_grid.append(modified_line)
    return modified_grid

# Define the grid
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

# Define colors dictionary
colors = [
    '\033[95m',   # Pink
    '\033[38;5;208m',  # Orange
    '\033[91m',   # Red
    '\033[96m'    # Cyan
]

# Modify and print the grid with colors
modified_grid = modify_grid(grid, colors)
for line in modified_grid:
    print(line)

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

# Modify and print the grid with the specified color
# for each in colors:
#
#     modified_grid = modify_grid(grid, each)
#     for line in modified_grid:
#         for num in enumerate(range(15)):
#             clear()
#             print(f'{"\t"*num}{line}')
#             time.sleep(.5)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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


def animate():


    # Animation loop
    for color in colors:
        modified_grid = modify_grid(grid, color)
        for offset in range(10):
            clear()
            if offset%2==1:
                print('')
            elif offset%3==2:
                print('')
                print('')

            for line in modified_grid:
                print(f'\t' * offset + line)
            time.sleep(0.3)


animate()
print_initials()
