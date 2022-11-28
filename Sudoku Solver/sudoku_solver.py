# ----------------------FINDING ROW AND COLUMN OF NEXT EMPTY SPACE---------------
def next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

# -------------------------CHECKING IF THE GUESSED NUMBER IS VALID OR NOT-----------------


def is_valid(puzzle, guess, row, col):

    # Checking in row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Checking in columns
    col_vals = []
    for r in range(9):
        col_vals.append(puzzle[r][col])

    if guess in col_vals:
        return False

    # Checking the 3x3 boxes
    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True


# ------------------------THE MAIN FUNCTION-------------------
def sudoku_solver(puzzle):

    row, col = next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if sudoku_solver(puzzle):
                return True

        puzzle[row][col] = -1

    return False


puzzle = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

if sudoku_solver(puzzle):
    print(puzzle)
else:
    print("SORRY, it can't be solved!!")