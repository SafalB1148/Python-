import random


# Function to print the structure of the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Function to check if a player has won
def check_winner(board, player):
    # Check rows for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns for a win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Function to check if the board is full (draw)
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


# Function to get available moves as a list of (row, col) tuples
def get_available_moves(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))
    return available_moves


# Function for the agent to make a move (random strategy)
def agent_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)


# Main function to run the Tic-Tac-Toe game
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    print("Welcome to Tic-Tac-Toe!")
    print("Enter your move as two numbers separated by space (e.g., '1 2' for row 1, column 2)")

    current_player = 'X'  # Start with player X

    while True:
        print_board(board)

        if current_player == 'X':
            move_input = input("Your move (row col): ")
            try:
                move = tuple(map(int, move_input.split()))
                if not (0 <= move[0] < 3 and 0 <= move[1] < 3):
                    raise ValueError
            except ValueError:
                print("Invalid input. Enter two numbers between 0 and 2.")
                continue

            if board[move[0]][move[1]] != ' ':
                print("Invalid move. That spot is already taken. Try again.")
                continue

            board[move[0]][move[1]] = current_player
        else:
            print("Agent's move:")
            move = agent_move(board)
            board[move[0]][move[1]] = current_player
            print(f"Agent chose row {move[0]} and column {move[1]}")

        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (draw)
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


# Run the Tic-Tac-Toe game
tic_tac_toe()