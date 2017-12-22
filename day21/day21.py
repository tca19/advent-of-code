#!/usr/bin/env python3

import os.path

def load_rules(filename):
    """Read filename to get all the rules (pattern transformation)."""
    rules = {}
    with open(filename) as f:
        for line in f:
            pattern_in, pattern_out = line.split("=>")
            rules[pattern_in.strip()] = pattern_out.strip()

    return rules

def rotate(pattern):
    """Perform a 90 degree clockwise rotation of pattern. Assume pattren is in
    the form ... / ... """
    grid   = pattern.split("/")
    n_cols = len(grid)
    new = []
    # columns become rows
    for i in range(n_cols):
        col = ""
        for j in range(n_cols-1, -1, -1):
            col += grid[j][i]
        new.append(col)

    return "/".join(new)

def flip(pattern):
    """Vertically flip pattern. Assume pattren is in the form ... / ... """
    grid = pattern.split("/")
    new = []
    for i in range(len(grid)):    # for each row
        new.append(grid[i][::-1]) # add the mirrored row (relative to middle)

    return "/".join(new)

def find_pattern(pattern, rules):
    """Find the correct transformation of pattern. If needed, rotate or flip
    pattern to find the appropriate transformation."""
    if pattern in rules:
        return rules[pattern]

    for i in range(4):
        f = flip(pattern)
        if f in rules:
            return rules[f]

        pattern = rotate(pattern)
        if pattern in rules:
            return rules[pattern]

    print("pattern not found")
    print(pattern)

def one_iteration(grid, rules):
    """Separate the grid into squares, apply transformation to each square, then
    create the new grid."""

    # grid -> squares
    squares = []
    n = len(grid)
    if n % 2 == 0: # divide grid into 2x2 squares. iterate rows then columns
        for j in range(0, n, 2):
            row = []
            for i in range(0, n, 2):
                square = grid[j][i:i+2] + "/" + grid[j+1][i:i+2]
                row.append(square)
            squares.append(row)

    else: #divide grid into 3x3 squares
        for j in range(0, n, 3):
            row = []
            for i in range(0, n, 3):
                square = grid[j][i:i+3] + "/" + grid[j+1][i:i+3] + "/" + \
                         grid[j+2][i:i+3]
                row.append(square)
            squares.append(row)

    # transform each square
    n = len(squares)
    for i in range(n):
        for j in range(n):
            squares[i][j] = find_pattern(squares[i][j], rules)

    # squares -> grid
    square_size = len(squares[0][0].split("/"))
    new_grid = []
    for row in range(len(squares)):
        for i in range(square_size):
            line = ""
            for j in range(len(squares[row])):
                line += squares[row][j].split("/")[i]
            new_grid.append(line)

    return new_grid

def generate_fractal(pattern, rules):
    """Use the start pattern and the rules to generate 5 fractal iterations."""

    for i in range(18):
        c = "".join(pattern).count("#")
        print("Iteration", i, "#", c)
#        print("\n".join(pattern))
        pattern = one_iteration(pattern, rules)

    # count number of # in last pattern
    c = "".join(pattern).count("#")
    return c

if __name__ == "__main__":
    filename = "day21_input.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        rules = load_rules(filename)
        start = ".#./..#/###".split("/")
        part_1 = generate_fractal(start, rules)
        print("PART ONE:", part_1)
