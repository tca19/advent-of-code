#!/usr/bin/env python3

import os.path

def contaminate(grid, n_burst=1, evolved=False):
    """Simulate n_burst steps of node contamination."""

    # expand grid and copy grid nodes into new grid
    n = len(grid)
    border = 100*n
    new_grid = [["." for _ in range(border*2+n)] for _ in range(border*2+n)]
    for i in range(n):
        for j in range(n):
            new_grid[i+border][j+border] = grid[i][j]
    grid = new_grid[:]

    # starting position of virus (center of grid)
    x = len(grid) // 2
    y = len(grid[0]) // 2

    # direction = 0 (north) / 1 (east) / 2 (south) / 3 (west)
    # turning right = +1
    # turning left  = -1
    # reverse       = +2
    direction = 0
    x_move = [-1, 0, 1, 0]
    y_move = [0, 1, 0, -1]
    n_infection = 0

    if not evolved:
        for i in range(n_burst):
            #print(i, x, y, n_burst)
            if grid[x][y] == "#":
                #print("node", x, y, "is infected. turning right")
                grid[x][y] = "." # clean node
                direction = (direction + 1) % 4
            else:
                #print("node", x, y, "is clean. turning left")
                grid[x][y] = "#" # infect node
                n_infection += 1
                direction = (direction - 1) % 4

            x += x_move[direction]
            y += y_move[direction]

           # print("after burst", i)
           # print(x, y, direction)
           # for line in grid:
           #     print(line)

           # ##print()
            #print(n_infection)

        return n_infection

if __name__ == "__main__":
    filename = "day22_infected.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        grid = open(filename).read().strip().split("\n")
        grid = "..#\n#..\n...".split("\n")
        grid = [list(line) for line in grid]
        part_1 = contaminate(grid, n_burst=10000)
        #part_2 = contaminate(grid, 7, evolved=False)
        print("PART ONE:", part_1)
#        print("PART TWO:", part_2)
