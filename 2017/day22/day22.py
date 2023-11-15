#!/usr/bin/env python3

import os.path

def contaminate(grid, n_burst, evolved=False):
    """Simulate n_burst steps of node contamination."""

    # expand grid (add borders of clean nodes). copy original grid into new grid
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

    # not evolved = part 1
    if not evolved:
        for i in range(n_burst):
            if grid[x][y] == "#":
                grid[x][y] = "." # clean node
                direction = (direction + 1) % 4

            else:
                grid[x][y] = "#" # infect node
                direction = (direction - 1) % 4
                n_infection += 1

            x, y = x + x_move[direction], y + y_move[direction]

        return n_infection

    # evolved = part 2
    for i in range(n_burst):
        if grid[x][y] == ".":   # clean -> weakened, turn left
            grid[x][y] = "W"
            direction = (direction - 1) % 4

        elif grid[x][y] == "W": # weakened -> infected, same direction
            grid[x][y] = "#"
            n_infection += 1

        elif grid[x][y] == "#": # infected -> flagged, turn right
            grid[x][y] = "F"
            direction = (direction + 1) % 4

        else:                   # flagged -> clean, reverse direction
            grid[x][y] = "."
            direction = (direction + 2) % 4

        x, y = x + x_move[direction], y + y_move[direction]

    return n_infection

if __name__ == "__main__":
    filename = "day22_infected.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        grid = open(filename).read().strip().split("\n")
        grid = [list(line) for line in grid]
        part_1 = contaminate(grid, 10000)
        print("PART ONE:", part_1)
        part_2 = contaminate(grid, 10000000, evolved=True)
        print("PART TWO:", part_2)
