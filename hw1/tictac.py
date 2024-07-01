"""
 Vincent de Torres
CS87A-Summer 2024 

This program demonstrates printing tic-tac-toe boards with scaled spacing between characters.

Functions:
- print_tic_tac_toe_board(board, scale): Print a tic-tac-toe board with scaled spacing between characters.

"""

def print_tic_tac_toe_board(board, scale):
    """
    Print a tic-tac-toe board with scaled spacing between characters.
    
    Args:
    - board (list of lists): The tic-tac-toe board represented as a 2D list of characters ('X', 'O', or other).
    - scale (int): The scaling factor for spacing between characters.
    """
    size = len(board)
    for i in range(size):
        row_str = ''
        for j in range(size):
            # Use 'X' and 'O' for the board representation
            row_str += board[i][j] + ' ' * scale
        print(row_str.rstrip())
        if i < size - 1:
            print(' ' * (size * scale))  # Extra spaces between rows
    print()

def main():
    # Define the tic-tac-toe boards with different winning combinations
    boards = [
        # Winning combination 1: Diagonal from top-left to bottom-right
        [
            ['X', 'O', 'O'],
            ['O', 'X', 'O'],
            ['O', 'O', 'X']
        ],
        # Winning combination 2: Vertical win
        [
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
            ['O', 'O', 'X']
        ],
        # Winning combination 3: Horizontal win
        [
            ['X', 'O', 'X'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O']
        ]
    ]

    # Define the scales for spacing between characters
    scales = [1, 2, 3]  # Adjust as needed for spacing

    # Print each board with increasing spacing
    for i, board in enumerate(boards):
        scale = scales[i]
        print(f"Board {i + 1} (Scale {scale}):")
        print_tic_tac_toe_board(board, scale)

if __name__ == "__main__":
    main()
