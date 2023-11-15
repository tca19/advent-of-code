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
    """Compute the Knot Hash of message."""

    ascii_codes = [str(ord(c)) for c in message]
    ascii_codes = ','.join(ascii_codes + ["17", "31", "73", "47", "23"])

    numbers  = list(range(256))
    position = skip_size = 0

    # do 64 rounds
    for _ in range(64):
        position, skip_size, _ =  knot_round(ascii_codes, numbers,
                                             position, skip_size)

    # sparse hash (256 elements) => deep hash (16 elements)
    deep_hash = []
    for i in range(0, 256, 16):
        xor = 0
        for j in range(16):
            xor ^= numbers[i+j]
        deep_hash.append(xor)

    hex_hash = ''.join([hex(x)[2:] for x in deep_hash])

    return hex_hash

if __name__ == '__main__':
    filename = "day10_lengths.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lengths = open(filename).read().strip()
        _, _, part_1 = knot_round(lengths, list(range(256)))
        print("PART ONE:", part_1)
        part_2 = knot_hash(lengths)
        print("PART TWO:", part_2)
