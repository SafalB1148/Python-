# Function to display the game board
def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


# Function to check if a player has won
def check_winner(board, player):
    # Winning combinations
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    # Return True if the player has a winning combination
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    # If all positions are filled with "X" or "O", it's a draw
    return all(pos in ["X", "O"] for pos in board)


# Main game function
def play_game():
    # Initialize the game board (positions 1-9)
    board = [str(i + 1) for i in range(9)]

    # Set the starting player to "X"
    current_player = "X"

    # Game loop
    while True:
        # Display the current game board
        display_board(board)

        # Ask the player for a move
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Check if the chosen position is valid (not already taken)
        if move < 0 or move > 8 or board[move] in ["X", "O"]:
            print("Invalid move! Try again.")
            continue

        # Make the move (place the player's mark on the board)
        board[move] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

    # Ask if the players want to play again
    if input("Play again? (y/n): ").lower() == "y":
        play_game()


# Start the game
play_game()
