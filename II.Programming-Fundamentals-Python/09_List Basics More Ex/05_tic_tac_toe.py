# • 0 - empty space
# • 1 - first player move
# • 2 - second player move

# Read input for the 3x3 tic-tac-toe board
board = [list(map(int, input().split())) for _ in range(3)]


# Check rows, columns, and diagonals for a winner
def check_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Determine the result based on the winning conditions
if check_winner(1):
    print("First player won")
elif check_winner(2):
    print("Second player won")
else:
    print("Draw!")

