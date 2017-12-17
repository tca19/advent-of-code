#!/usr/bin/env python3

import os.path

def n_matches(valA, valB):
    """Return number of value matches between generator A and generator B."""

    n = 0
    mulA, mulB, p = 16807, 48271, 2**31 - 1

    for _ in range(40000000):
        valA = (valA * mulA) % p
        valB = (valB * mulB) % p

        if (valA &  0xFFFF) == (valB &  0xFFFF): # same last 16 bits
            n += 1

    return n

def n_matches_condition(valA, valB):
    """Return number of value matches between generator A and generator B, but
    they both have a special condition when generating numbers."""

    n = 0
    mulA, mulB, p = 16807, 48271, 2**31 - 1

    for _ in range(5000000):
        valA = (valA * mulA) % p
        while (valA & 0b11) > 0:     # regenerate until it's a multiple of 4
            valA = (valA * mulA) % p

        valB = (valB * mulB) % p
        while (valB & 0b111) > 0:    # regenerate until it's a multiple of 8
            valB = (valB * mulB) % p

        if (valA &  0xFFFF) == (valB &  0xFFFF): # same last 16 bits
            n += 1

    return n


if __name__ == '__main__':
    filename = "day15_seeds.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        seeds = open(filename).read().split()
        seedA, seedB = int(seeds[4]), int(seeds[9])
#        seedA, seedB = 65, 8921
        part_1 = n_matches(seedA, seedB)
        part_2 = n_matches_condition(seedA, seedB)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
