#!/usr/bin/env python3

import os.path

def knot_round(lengths, numbers, position=0, skip_size=0):
    """Process one round of knot hash algorithm on numbers list."""

    n = 256 # size of numbers array

    for length in list(map(int, lengths.split(","))):
        end = position + length

        if end < n:
            numbers[position:end] = numbers[position:end][::-1]
        else:
            rev_sublist = (2 * numbers)[position:end][::-1]
            numbers[position:] = rev_sublist[:n-position]
            numbers[:end%n] = rev_sublist[n-position:]

        position = (position + length + skip_size) % n
        skip_size += 1

    return position, skip_size, numbers[0] * numbers[1]

def knot_hash(message):
    """Compute the knot-hash of message. Return the binary string of hash."""

    ascii_codes = [str(ord(c)) for c in message]
    ascii_codes = ','.join(ascii_codes + ["17", "31", "73", "47", "23"])

    numbers  = list(range(256))
    position = skip_size = 0

    # do 64 rounds
    for _ in range(64):
        position, skip_size, _ =  knot_round(ascii_codes, numbers,
                                     position=position, skip_size=skip_size)

    # sparse hash (256 elements) => deep hash (16 elements)
    deep_hash = []
    for i in range(0, 256, 16):
        xor = 0
        for j in range(16):
            xor ^= numbers[i+j]
        deep_hash.append(xor)

    bin_hash = ''.join(["{:0>8}".format(bin(x)[2:]) for x in deep_hash])

    return bin_hash

def n_bits_1(message):
    """Compute number of bits equal to 1 in all binary knot hashes of message-0
    to message-127. Return the grid formed by all hashes as well."""

    grid = [knot_hash("{}-{}".format(message, i)) for i in range(128)]
    n    = sum([row.count("1") for row in grid])

    return n, grid

def visit_region(grid, seen, i, j):
    """Start at (i,j), mark all points of the same region as seen."""

    # already seen, nothing more to do
    if seen[i][j]:
        return

    seen[i][j] = True

    # not in the same region, no need to see neighbors
    if grid[i][j] == "0":
        return

    # visit each 4 neighbors
    if i > 0:
        visit_region(grid, seen, i-1, j)
    if i < 127:
        visit_region(grid, seen, i+1, j)
    if j > 0:
        visit_region(grid, seen, i, j-1)
    if j < 127:
        visit_region(grid, seen, i, j+1)

def number_regions(grid):
    """Find the number of independant regions of '1' in grid."""

    seen = [[False for _ in range(128)] for _ in range(128)]
    n = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j] == "1" and not seen[i][j]:
                n += 1
                visit_region(grid, seen, i, j)

    return n

if __name__ == '__main__':
    filename = "day14_string.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        string = open(filename).read().strip()
        part_1, grid = n_bits_1(string)
        part_2 = number_regions(grid)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
