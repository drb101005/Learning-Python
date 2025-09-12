def create_grid(size):
    # Create an empty grid with '.' representing unoccupied spaces
    return [['.' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    # Print the current state of the grid
    for row in grid:
        print(" ".join(row))
    print("\n")

def is_valid_position(row, col, blocked_rows, blocked_cols, blocked_diag1, blocked_diag2):
    # Check if the position is not blocked by rows, columns, or diagonals
    return row not in blocked_rows and col not in blocked_cols and (row - col) not in blocked_diag1 and (row + col) not in blocked_diag2

def backtrack(row, size, blocked_rows, blocked_cols, blocked_diag1, blocked_diag2, queen_positions, grid):
    # If all queens are placed, return True (solution found)
    if row == size:
        return True

    # Try every column in the current row
    for col in range(size):
        if is_valid_position(row, col, blocked_rows, blocked_cols, blocked_diag1, blocked_diag2):
            # Place the queen at (row, col)
            queen_positions.append((row, col))
            blocked_rows.add(row)
            blocked_cols.add(col)
            blocked_diag1.add(row - col)  # Top-left to bottom-right diagonal
            blocked_diag2.add(row + col)  # Top-right to bottom-left diagonal

            # Update grid with queen at (row, col)
            grid[row][col] = 'x'

            # Print the current grid state
            print(f"After placing queen at row {row+1}, col {col+1}:")
            print_grid(grid)

            # Recur to place queens in the next row
            if backtrack(row + 1, size, blocked_rows, blocked_cols, blocked_diag1, blocked_diag2, queen_positions, grid):
                return True

            # Backtrack: remove the queen and unblock the positions
            queen_positions.pop()
            blocked_rows.remove(row)
            blocked_cols.remove(col)
            blocked_diag1.remove(row - col)
            blocked_diag2.remove(row + col)

            # Reset the grid position to '.'
            grid[row][col] = '.'

    return False

def place_queens(n):
    blocked_rows = set()
    blocked_cols = set()
    blocked_diag1 = set()
    blocked_diag2 = set()
    queen_positions = []
    
    # Create the grid
    grid = create_grid(n)

    # Start the backtracking from the first row
    if backtrack(0, n, blocked_rows, blocked_cols, blocked_diag1, blocked_diag2, queen_positions, grid):
        return queen_positions
    else:
        return None

# Example: Solve for 4 queens
n = 4
placed_queen_positions = place_queens(n)
if placed_queen_positions:
    print("Positions of all placed queens:", placed_queen_positions)
else:
    print("No solution found.")
