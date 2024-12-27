def print_board(board):
    """Helper function to print the chessboard."""
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, row, n):
    """Solve the N-Queens problem using backtracking."""
    if row == n:
        print_board(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            # Recurse to place queens in the next row
            res = solve_n_queens(board, row + 1, n) or res
            # Backtrack and remove the queen
            board[row][col] = '.'

    return res

def eight_queens():
    """Main function to solve the 8-Queens problem."""
    n = 8
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

# Run the function
eight_queens()
