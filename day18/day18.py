#!/usr/bin/env python3

import os.path
from collections import defaultdict

def convert_value(s, registers):
    """Convert s to integer value, or look its value in registers."""
    try:
        X = int(s)
    except:
        X = registers[s]

    return X

def recover_frequency(instructions):
    """Process each instructions. Store all played frequencies. Return the last
    played frequency when the first "rcv" instruction is met."""

    registers = defaultdict(int)
    played_freq = []
    pos = 0

    while True:
        row = instructions[pos].split()

        if row[0] == "snd":
            X = convert_value(row[1], registers)
            played_freq.append(X)

        if row[0] == "set":
            Y = convert_value(row[2], registers)
            registers[row[1]] = Y

        if row[0] == "add":
            Y = convert_value(row[2], registers)
            registers[row[1]] += Y

        if row[0] == "mul":
            Y = convert_value(row[2], registers)
            registers[row[1]] *= Y

        if row[0] == "mod":
            Y = convert_value(row[2], registers)
            registers[row[1]] %= Y

        if row[0] == "rcv":
            X = convert_value(row[1], registers)
            if X != 0:
                return played_freq[-1]

        if row[0] == "jgz":
            X = convert_value(row[1], registers)
            Y = convert_value(row[2], registers)

            if X > 0:
                pos += Y - 1

        pos += 1

if __name__ == "__main__":
    filename = "day18_instructions.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        instructions = open(filename).read().split("\n")
        part_1 = recover_frequency(instructions)
        print("PART ONE:", part_1)
