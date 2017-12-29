#!/usr/bin/env python3

import os.path

def n_matches(valA, valB, n_pairs, criteria=False):
    """Return number of value matches between generator A and generator B after
    n_pairs generated."""

    n = 0
    mulA, mulB, p = 16807, 48271, 2**31 - 1

    for _ in range(n_pairs):
        valA = (valA * mulA) % p
        valB = (valB * mulB) % p

        # regenerate until it's a multiple of 4 (for part 2)
        while criteria and (valA & 0b11) > 0:
            valA = (valA * mulA) % p
        # regenerate until it's a multiple of 8 (for part 2)
        while criteria and (valB & 0b111) > 0:
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
        part_1 = n_matches(seedA, seedB, 40000000)
        print("PART ONE:", part_1)
        part_2 = n_matches(seedA, seedB, 5000000, True)
        print("PART TWO:", part_2)
