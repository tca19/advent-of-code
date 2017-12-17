#!/usr/bin/env python3

import sys

def distance_to_1(n):
    """Return the distance between cell (n) and center of grid (1)."""

    # find the ring size of cell n
    if int(n**0.5)**2 == n and n%2 == 1: # special case, odd square numbers
        size_ring = int(n**0.5)
    else:
        size_ring = int(n**0.5) + (int(n**0.5)%2) + 1

    # find the side of the ring  on which cell n is. Once we have the side, we
    # can compute the distance
    if n > size_ring**2 - 1*(size_ring - 1): # n is on bottom side
        center = size_ring**2 - size_ring//2 # center of bottom side
        hor_dist = abs(center-n) # horizontal distance between n and center 1
        ver_dist = size_ring//2  # vertical distance between n and center 1
    elif n > size_ring**2 - 2*(size_ring - 1): # n is on left side
        hor_dist = size_ring//2
        center = size_ring**2 - size_ring + 1 - hor_dist
        ver_dist = abs(n - center)
    elif n > size_ring**2 - 3*(size_ring - 1): # n is on top side
        ver_dist = size_ring//2
        center = size_ring**2 - 2*(size_ring - 1) - ver_dist
        hor_dist = abs(n - center)
    else: # n is on right side
        hor_dist = size_ring//2
        center = (size_ring-2)**2 + hor_dist
        ver_dist = abs(n - center)

    return hor_dist + ver_dist

def sum_adjacent(x, y, grid):
    """Return sum of values in all adjacent cell to (x, y)."""
    s = grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1] \
      + grid[x  ][y-1] +      0       + grid[x  ][y+1] \
      + grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1]

    return s

def find_larger_value(n):
    """Build a spiral grid where all new value is the sum of current
    adjacent cells. Find the first new value larger than n."""

    grid = [ [0 for _ in range(22)] for _ in range(22) ]
    grid[10][10] = 1  # origin of spiral grid is placed at (10, 10)
    x, y = 10, 10

    # build each new value of current ring. Start with left side, then top,
    # right and finally bottom side. Stop once we have a value larger than n
    for size_ring in range(3, 20, 2):
        # first cell of new ring
        y += 1
        grid[x][y] = sum_adjacent(x, y, grid)
        if grid[x][y] > n:
            return grid[x][y]

        # build left side
        for _ in range(1, size_ring-1):
            x -= 1
            grid[x][y] = sum_adjacent(x, y, grid)
            if grid[x][y] > n:
                return grid[x][y]

        # build top side
        for _ in range(1, size_ring):
            y -= 1
            grid[x][y] = sum_adjacent(x, y, grid)
            if grid[x][y] > n:
                return grid[x][y]

        # build right side
        for _ in range(1, size_ring):
            x += 1
            grid[x][y] = sum_adjacent(x, y, grid)
            if grid[x][y] > n:
                return grid[x][y]

        # build bottom side
        for k in range(1, size_ring):
            y += 1
            grid[x][y] = sum_adjacent(x, y, grid)
            if grid[x][y] > n:
                return grid[x][y]

if __name__ == "__main__":
    number = 277678
    part_1 = distance_to_1(number)
    part_2 = find_larger_value(number)
    print("PART ONE:", part_1)
    print("PART TWO:", part_2)
