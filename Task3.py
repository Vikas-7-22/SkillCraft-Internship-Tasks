def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    row, col = pos
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False

print("Enter the Sudoku puzzle row by row (use 0 for empty cells).")
sudoku_grid = []
for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != 9:
        print("⚠ Each row must have exactly 9 numbers.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    sudoku_grid.append(row)

print("\nUnsolved Sudoku:")
print_grid(sudoku_grid)

if solve(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")