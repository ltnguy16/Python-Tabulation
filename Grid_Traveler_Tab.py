#grid traveler using fibanocci

def grid_traveler_tab(x, y):
  #initialize grid
  grid = [[0 for i in range(x+2)] for j in range(y+2)]
  grid[1][1] = 1

  for i in range(x+1):
    for j in range(y+1):
      current = grid[i][j]
      if (i + 1 <= x): grid[i + 1][j] += current
      if (j + 1 <= y): grid[i][j + 1] += current
  return grid[x][y]

"""
print(grid_traveler_tab(1,1))
print(grid_traveler_tab(2,3))
print(grid_traveler_tab(3,2))
print(grid_traveler_tab(3,3))
print(grid_traveler_tab(18,18))
"""