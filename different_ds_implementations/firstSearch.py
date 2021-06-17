# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # covered -> the grid space we have seen
    covered = [[0 for _ in grid[0]] for _ in grid]
    covered[init[0]][init[1]] = 1 # Start point

    g_value = 0
    start = init
    path = [[g_value] + init]
    found = False
    resign = False
    while found is False and resign is False:
        # go with the lowest g_value:
        path.sort()
        path.reverse()
        start_yxg = path.pop()
        start = [start_yxg[1], start_yxg[2]]
        g_value = start_yxg[0]
        if start == goal:
            found = True
            return start_yxg
        else:
            for d in delta:
                cell = [start[0] + d[0], start[1] + d[1]]
                if cell[0] >= 0 and cell[0] < len(grid) and cell[1] >=0 and cell[1] < len(grid[0]):
                    if grid[cell[0]][cell[1]] == 0 and covered[cell[0]][cell[1]] == 0:
                        new_g = g_value + cost
                        path.append([new_g] + cell)
                        covered[cell[0]][cell[1]] = 1
    return 'fail'


search(grid,init,goal,cost)
