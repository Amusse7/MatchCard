import random

cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
random.shuffle(cards)

def display_board(board):
    for row in board:
        print(" ".join(row))

def initialize_board():
    board = []
    for _ in range(4):
        row = ['*'] * 4
        board.append(row)
    return board

def play_game():
    board = initialize_board()
    display_board(board)
    matched = set()
    attempts = 0

    while len(matched) < len(cards):
        try:
            print("\nEnter the row and column number (e.g., '1 2'):")
            row1, col1 = map(int, input("Enter position of the first card: ").split())
            row2, col2 = map(int, input("Enter position of the second card: ").split())

            if (row1 == row2 and col1 == col2) or board[row1 - 1][col1 - 1] != '*' or board[row2 - 1][col2 - 1] != '*':
                print("Invalid input or cards already matched! Try again.")
                continue

            if cards[(row1 - 1) * 4 + (col1 - 1)] == cards[(row2 - 1) * 4 + (col2 - 1)]:
                board[row1 - 1][col1 - 1] = cards[(row1 - 1) * 4 + (col1 - 1)]
                board[row2 - 1][col2 - 1] = cards[(row2 - 1) * 4 + (col2 - 1)]
                matched.add(cards[(row1 - 1) * 4 + (col1 - 1)])
                print("Match found!")
            else:
                print("No match! Try again.")
            
            display_board(board)
            attempts += 1
        except (ValueError, IndexError):
            print("Invalid input! Please enter valid row and column numbers.")

    print(f"Congratulations! You've matched all cards in {attempts} attempts.")

play_game()
