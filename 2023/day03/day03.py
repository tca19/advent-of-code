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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse
import re


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
    x, y, length, _ = number

    # Check left side.
    if grid[x][y-1] != ".":
        symbols.append(grid[x][y-1])

    # Check bottom side.
    for j in range(y-1, y-1 + (length+2)):
        if grid[x+1][j] != ".":
            symbols.append(grid[x+1][j])

    # Check right side.
    if grid[x][y+length] != ".":
        symbols.append(grid[x][y+length])

    # Check top side.
    for j in range(y-1, y-1 + (length+2)):
        if grid[x-1][j] != ".":
            symbols.append(grid[x-1][j])

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
