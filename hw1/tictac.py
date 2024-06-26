def print_tic_tac_toe_board(board, scale):
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

    # Define the scale for spacing between characters
    scale = 3  # Adjust as needed for spacing

    # Print each board with uniform spacing
    for i, board in enumerate(boards):
        print(f"Board {i + 1} (Scale {scale*i}):")
        print_tic_tac_toe_board(board, scale*i)

if __name__ == "__main__":
    main()
