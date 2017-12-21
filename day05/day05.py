#!/usr/bin/env python3

import os.path

def n_steps(array, specific_condition=False):
    """Compute number of steps required to escape array"""

    step = i = 0

    while -1 < i < len(array):
        offset = array[i]

        if specific_condition and offset >= 3:
            array[i] -= 1
        else:
            array[i] += 1

        i += offset
        step += 1

    return step

if __name__ == '__main__':
    filename = "day05_jumps.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lines = open(filename).read().split()
        offsets = list(map(int, lines))
        part_1 = n_steps(offsets[:])
        print("PART ONE:", part_1)
        part_2 = n_steps(offsets, specific_condition=True)
        print("PART TWO:", part_2)
