import os
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


def initialize_grid(size, fill_char='██ '):
    """Initialize a square grid with the specified size and fill character."""
    return [[fill_char for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    """Print the grid with coordinates."""
    size = len(grid)

    # Print the top coordinates
    top_coords = '   ' + ''.join(f'{x:2} ' for x in range(size))
    print(top_coords)

    for y, row in enumerate(grid):
        # Print the side coordinates
        row_with_coords = f'{y:2} ' + ''.join(row)
        print(row_with_coords)


def toggle_shade(grid, x, y, dark_char='▓▓ ', light_char='░░ '):
    """Toggle the shade of a specific coordinate on the grid."""
    if 0 <= x < len(grid) and 0 <= y < len(grid):
        grid[y][x] = dark_char if grid[y][x] == light_char else light_char

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_mode(grid):
    """Enter interactive mode to toggle shades of coordinates."""
    print("Interactive mode: Enter coordinates as 'x y' to toggle shade. Enter 'q' to quit and save.")

    first_iteration = True

    while True:
        if not first_iteration:
            clear_screen()
        else:
            first_iteration = False

        print_grid(grid)
        user_input = input("Enter coordinates (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        try:
            x, y = map(int, user_input.split())
            toggle_shade(grid, x, y)
        except ValueError:
            print("Invalid input. Please enter coordinates in the format 'x y'.")


def save_coordinates(grid, dark_char='▓▓ '):
    """Save the coordinates of the shaded cells."""
    coords = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == dark_char]
    return coords


def load_coordinates(grid, coords, dark_char='▓▓ '):
    """Load the coordinates of the shaded cells into the grid."""
    for x, y in coords:
        if 0 <= x < len(grid) and 0 <= y < len(grid):
            grid[y][x] = dark_char


# Configuration
size = 15  # This determines both the width and height of the square grid

# Initialize the grid
grid = initialize_grid(size)

# Enter interactive mode
interactive_mode(grid)

# Save the coordinates of the shaded cells
shaded_coords = save_coordinates(grid)
print("Shaded coordinates:", shaded_coords)

# To demonstrate loading the coordinates, we can reset the grid and load the saved coordinates
new_grid = initialize_grid(size)
load_coordinates(new_grid, shaded_coords)

# Print the new grid to verify that the coordinates have been loaded correctly
print("Grid after loading saved coordinates:")
print_grid(new_grid)

"""
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 
 0 ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ 
 1 ██ ██ ██ ██ ██ ██ ░░ ░░ ░░ ██ ██ ██ ██ ██ ██ 
 8 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 3 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██
 4 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 6 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 7 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 8 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 9 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
10 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
11 ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ 
12 ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ 
13 ██ ██ ░░ ░░ ░░ ██ ░░ ░░ ░░ ██ ░░ ░░ ░░ ██ ██ 
14 ██ ██ █░ ░░ ░█ ██ █░ ░░ ░█ ██ █░ ░░ ░█ ██ ██  
15 ██ ██ ██ ░░ ██ ██ ██ ░░ ██ ██ ██ ░░ ██ ██ ██

"""
canvas_string="""
 ██ ██ ██ ██ ██ ██ ░░ ░░ ░░ ██ ██ ██ ██ ██ ██ 
 ██ ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ ██ 
 ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ 
 ██ ██ ██ ░░ ░█ ██ █░ ░░ ░░ ░░ ░█ ██ █░ ██ ██
 ██ ██ ░░ ░░ ▒█ ██    ░░ ░░ ░░ ▒█ ██    ██ ██
 ██ ██ ░░ ░░ ▒█ ██ █▒ ░░ ░░ ░░ ▒█ ██ █▒ ██ ██ 
 ██ ██ ░░ ░░ ░█ ██ █░ ░░ ░░ ░░ ░█ ██ █░ ██ ██ 
 ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ 
 ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ 
 ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██   
 ██ ██ ░░ ░░ ░░ ██ ░░ ░░ ░░ ██ ░░ ░░ ░░ ██ ██ 
 ██ ██ █░ ░░ ░█ ██ █░ ░░ ░█ ██ █░ ░░ ░█ ██ ██  
 ██ ██ ██ ░░ ██ ██ ██ ░░ ██ ██ ██ ░░ ██ ██ ██
 """
print(canvas_string)
canvas_list=canvas_string.split('\n')


print("\n".join(canvas_list))
# print(f"{[each for each in canvas_list if each.strip()]}",end='\n')
# Define ANSI escape codes for colors
# Define ANSI escape codes for colors
# Define ANSI escape codes for colors
colors = {
    'light_pink': '\033[95m',
    'orange': '\033[38;5;208m',  # ANSI escape code for more orangey color
     'red': '\033[91m',
    'cyan': '\033[96m'
}



# Define Pacman ghost representations
pacman_ghosts = {
    'light_pink': [
        " ██████████████████ ",
        " ██████████████████ ",
        " ██              ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██              ██ ",
        " ██████████████████ ",
        " ██████████████████ "
    ],
    'orange': [
        " ██████████████████ ",
        " ██████████████████ ",
        " ██              ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██              ██ ",
        " ██████████████████ ",
        " ██████████████████ "
    ],
    'light_blue': [
        " ██████████████████ ",
        " ██████████████████ ",
        " ██              ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██              ██ ",
        " ██████████████████ ",
        " ██████████████████ "
    ],
    'red': [
        " ██████████████████ ",
        " ██████████████████ ",
        " ██              ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██              ██ ",
        " ██████████████████ ",
        " ██████████████████ "
    ],
    'cyan': [
        " ██████████████████ ",
        " ██████████████████ ",
        " ██              ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██  ██████████  ██ ",
        " ██              ██ ",
        " ██████████████████ ",
        " ██████████████████ "
    ]
}

# Print Pacman ghosts in different colors
for color, ghost in pacman_ghosts.items():
    print(colors[color] + "\n".join(ghost) + "\033[0m\n")
