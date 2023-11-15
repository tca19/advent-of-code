#!/usr/bin/env python3

import os.path
import string

def next_cell(x, y, direction):
    """Find coordinates of next cell given direction."""

    if direction == "N":
        return x-1, y
    if direction == "E":
        return x, y+1
    if direction == "S":
        return x+1, y
    if direction == "W":
        return x, y-1

def follow_path(lines):
    """Get every letters on the path. Compute length of path as well."""

    direction = "S" # starting point comes from the top, so direction is south
    x, y = 0, lines[0].index("|")
    word = ""
    n_steps = 0

    while True:
        c = lines[x][y]

        if c == " ":
            return word, n_steps

        elif c in string.ascii_letters:
            word += c

        elif c == "+":
            if direction in "NS":
                # can either go left or right
                if lines[x][y-1] != " ":
                    direction = "W"
                else:
                    direction = "E"

            else:
                # can either go up or down
                if lines[x-1][y] != " ":
                    direction = "N"
                else:
                    direction = "S"

        x, y = next_cell(x, y, direction)
        n_steps += 1

if __name__ == "__main__":
    filename = "day19_labyrinth.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        labyrinth = open(filename).read().split("\n")
        part_1, part_2 = follow_path(labyrinth)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
