#!/usr/bin/env python3

import os.path
from collections import defaultdict

def convert_value(s, registers):
    """Convert s to integer value, or look its value in registers."""

    try:
        return int(s)
    except:
        return registers[s]

def count_mul(instructions):
    """Return the number of times a mul instruction is executed."""

    pos, n_mul = 0, 0
    registers  = defaultdict(int)

    while -1 < pos < len(instructions)-1:
        row = instructions[pos].split()

        if row[0] == "set":
            registers[row[1]]  = convert_value(row[2], registers)

        if row[0] == "sub":
            registers[row[1]] -= convert_value(row[2], registers)

        if row[0] == "mul":
            registers[row[1]] *= convert_value(row[2], registers)
            n_mul += 1

        if row[0] == "jnz":
            if convert_value(row[1], registers) != 0:
                pos += convert_value(row[2], registers) - 1

        pos += 1

    return n_mul

def optimized_program(n):
    """Optimized reverse-engineered version of assembler instructions."""

    b = 100000 + 100*n
    c = b + 17000
    h = 0

    for b in range(b, c+1, 17):
        for d in range(2, int(b**0.5)+1):
            if b%d == 0: # b is non prime, increment h, move to next b
                h += 1
                break

    return h

if __name__ == "__main__":
    filename = "day23_instructions.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        instructions = open(filename).read().split("\n")
        part_1 = count_mul(instructions)
        print("PART ONE:", part_1)
        part_2 = optimized_program(int(instructions[0].split()[-1]))
        print("PART TWO:", part_2)
