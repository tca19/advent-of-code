#!/usr/bin/env python3

import os.path

def min_steps(path):
    """Compute the minimal number of steps required to arrive at same cell as
    path."""

    # x and y are hexmap coordinates
    x, y, max_distance = 0, 0, 0

    for direction in path:
        if direction == "n":
            y += 1
        elif direction == "ne":
            x += 1
            y += 1
        elif direction == "se":
            x += 1
        elif direction == "s":
            y -= 1
        elif direction == "sw":
            x -= 1
            y -= 1
        elif direction == "nw":
            x -= 1

        distance = max(abs(x), abs(y), abs(x-y))
        max_distance = max(max_distance, distance)

    steps = max(abs(x), abs(y), abs(x-y))
    return steps, max_distance

if __name__ == '__main__':
    filename = "day11_path.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        path = open(filename).read().strip().split(',')
        part_1, part_2 = min_steps(path)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
