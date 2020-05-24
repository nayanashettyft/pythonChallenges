import numpy

def solve_sudoku():
  global grid
  find = find_empty()
  if not find:
    return True
  else:
    row,col = find
  for n in range(1,10):
    if possible(row, col, n):
      grid[row][col] = n
      if solve_sudoku():
        return True
      grid[row][col] = 0
  return False

def find_empty():
  global grid
  for i in range(9):
    for j in range (9):
      if grid[i][j] == 0:
        return (i,j)

def possible(row, col, n):
  global grid
  # Check row
  for j in range(9):
    if grid[row][j] == n:
      return False
  # cheak column
  for i in range(9):
    if grid[i][col] == n:
      return False
  # check 3x3 box
  box_row = (row // 3) * 3
  box_col = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if grid[box_row + i][box_col + j] == n:
        return False
  return True


# sudoku_input = '5 3 0 0 7 0 0 0 0 6 0 0 1 9 5 0 0 0 0 9 8 0 0 0 0 6 0 8 0 0 0 6 0 0 0 3 4 0 0 8 0 3 0 0 1 7 0 0 0 2 0 0 0 6 0 6 0 0 0 0 2 8 0 0 0 0 4 1 9 0 0 5 0 0 0 0 8 0 0 7 9'
sudoku_input = '3 6 7 5 3 5 6 2 9 1 2 7 0 9 3 6 0 6 2 6 1 8 7 9 2 0 2 3 7 5 9 2 2 8 9 7 3 6 1 2 9 3 1 9 4 7 8 4 5 0 3 6 1 0 6 3 2 0 6 1 5 5 4 7 6 5 6 9 3 7 4 5 2 5 4 7 4 4 3 0 7 '
sudoku_input_arr = list(map(int,sudoku_input.split()))
print(sudoku_input_arr)
sudoku_grid = numpy.array(sudoku_input_arr)
grid = sudoku_grid.reshape(9,9)
if solve_sudoku():
  print(numpy.matrix(grid))
else:
  print("sorry cant solve")