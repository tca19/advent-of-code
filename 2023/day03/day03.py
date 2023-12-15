#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 3 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file representing a grid. In this grid, each line if composed
# of numbers and symbols.
#
# An example of such file is:
#
#   467..114..
#   ...*......
#   ..35..633.
#   ......#...
#   617*......
#   .....+.58.
#   ..592.....
#   ......755.
#   ...$.*....
#   .664.598..
#
# The first line contains the numbers 467 and 114, and no symbols.
# The second line only contains the symbol '*' ('.' is not considered as a
# symbol).
#
# Part 1
# ======
# We consider that a number in the grid is a "part number" if there is a symbol
# around it. The task is to find the sum of all "part numbers" in the grid.
#
# Part 2
# ======
# The grid contains some '*' symbols. A '*' symbol is called a "gear" if it is
# adjacent to exactly 2 "part numbers". Its "gear ratio" is the product of its
# 2 adjacent part numbers. The task is to find the sum of all gear ratios in
# the grid.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from collections import defaultdict
import argparse
import re

# Maps a gear position (x,y) to its list of adjacent part numbers.
GEARS: dict = defaultdict(list)


def find_numbers(grid: list) -> list:
    """
    Return the list of all found numbers in `grid`. Each number is a 4-tuple
    containing:
        - the start row
        - the start col
        - the length
        - the integer value

        Parameters:
            grid (list): A list of string. Each string is a line of the grid.

        Returns:
            numbers (list): A list of tuple. Each tuple contains 4 information
                            about a number (see function documentation).
    """
    numbers = []
    pattern = r"(\d+)"
    for i, row in enumerate(grid):
        for match in re.finditer(pattern, row):
            x = i
            y = match.start()
            length = len(match.group())
            value = int(match.group())
            numbers.append((x, y, length, value))

    return numbers


def find_symbols_around(number: tuple, grid: list) -> list:
    """
    Return the list of symbols around `number` in `grid`.

        Parameters:
            number (tuple): Information about the position and the length of
                            `number`to find it in the grid.
            grid (list): A list of string. Each string is a line of the grid.

        Returns:
            symbols (list): A list of all the symbols around `number` in the
                            `grid`.
    """
    symbols = []
    x, y, length, value = number

    # For Part 2, we need to find the '*' symbols that have exactly 2 adjacent
    # part numbers. So when we find a '*' during Part 1, we save in the global
    # variable GEARS that for this '*' symbol (at its position), `number` is
    # one of its adjacent neighbor. That way, we won't need to go through the
    # traversal of the grid a second time to find the "gears" needed in Part 2.

    # Check left side.
    if grid[x][y-1] != ".":
        symbols.append(grid[x][y-1])
        if grid[x][y-1] == "*":  # For Part 2
            GEARS[(x, y-1)].append(value)

    # Check bottom side.
    for j in range(y-1, y-1 + (length+2)):
        if grid[x+1][j] != ".":
            symbols.append(grid[x+1][j])
            if grid[x+1][j] == "*":  # For Part 2
                GEARS[(x+1, j)].append(value)

    # Check right side.
    if grid[x][y+length] != ".":
        symbols.append(grid[x][y+length])
        if grid[x][y+length] == "*":  # For Part 2
            GEARS[(x, y+length)].append(value)

    # Check top side.
    for j in range(y-1, y-1 + (length+2)):
        if grid[x-1][j] != ".":
            symbols.append(grid[x-1][j])
            if grid[x-1][j] == "*":  # For Part 2
                GEARS[(x-1, j)].append(value)

    return symbols


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day03.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    # Generate a grid from data. Add a "border" around the grid, so we don't
    # need to check negative/overflow indexes when looking "around" each cell
    # of the original grid.
    G = ["." * (len(data[0].strip())+2)]  # +2 because: left/right borders
    for line in data:
        G.append("." + line.strip() + ".")
    G.append("." * (len(data[0].strip()) + 2))  # +2 because: same reason

    all_numbers = find_numbers(G)
    part1 = sum(value for (x, y, length, value) in all_numbers
                if len(find_symbols_around((x, y, length, value), G)) > 0)
    print(f"Part 1: {part1}")

    part2 = sum(numbers[0] * numbers[1] for gear, numbers in GEARS.items()
                if len(numbers) == 2)
    print(f"Part 2: {part2}")
