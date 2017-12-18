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

    pos         = 0
    registers   = defaultdict(int)
    last_played = -1

    while True:
        row = instructions[pos].split()

        if row[0] == "snd":
            last_played = convert_value(row[1], registers)

        if row[0] == "set":
            registers[row[1]] = convert_value(row[2], registers)

        if row[0] == "add":
            registers[row[1]] += convert_value(row[2], registers)

        if row[0] == "mul":
            registers[row[1]] *= convert_value(row[2], registers)

        if row[0] == "mod":
            registers[row[1]] %= convert_value(row[2], registers)

        if row[0] == "rcv":
            if convert_value(row[1], registers) != 0:
                return last_played

        if row[0] == "jgz":
            if convert_value(row[1], registers) > 0:
                pos += convert_value(row[2], registers) - 1

        pos += 1

def concurrent_programs(instructions):
    """Simulate 2 concurrent programs running the instructions. Return the
    number of times program 1 send a value to program 0."""

    registers0 = defaultdict(int)
    registers1 = defaultdict(int)
    registers1["p"] = 1
    pos0 = 0
    pos1 = 0
    queue0 = []
    queue1 = []
    prog1_send = 0

    while True:
        row0 = instructions[pos0].split()
        row1 = instructions[pos1].split()

        # deadlock?
        if (row0[0] == "rcv" and row1[0] == "rcv"
            and len(queue0) == 0 and len(queue1) == 0):
            return prog1_send

        # process instruction on program 1
        if row1[0] == "snd":
            queue0.insert(0, convert_value(row1[1], registers1))
            prog1_send += 1

        if row1[0] == "set":
            registers1[row1[1]] = convert_value(row1[2], registers1)

        if row1[0] == "add":
            registers1[row1[1]] += convert_value(row1[2], registers1)

        if row1[0] == "mul":
            registers1[row1[1]] *= convert_value(row1[2], registers1)

        if row1[0] == "mod":
            registers1[row1[1]] %= convert_value(row1[2], registers1)

        if row1[0] == "rcv":
            if len(queue1) > 0:
                registers1[row1[1]] = queue1.pop()
            else: # no value to receive, stay at same instruction
                pos1 -= 1

        if row1[0] == "jgz":
            if convert_value(row1[1], registers1) > 0:
                pos1 += convert_value(row1[2], registers1) - 1

        pos1 += 1

        # process instruction on program 0
        if row0[0] == "snd":
            queue1.insert(0, convert_value(row0[1], registers0))

        if row0[0] == "set":
            registers0[row0[1]] = convert_value(row0[2], registers0)

        if row0[0] == "add":
            registers0[row0[1]] += convert_value(row0[2], registers0)

        if row0[0] == "mul":
            registers0[row0[1]] *= convert_value(row0[2], registers0)

        if row0[0] == "mod":
            registers0[row0[1]] %= convert_value(row0[2], registers0)

        if row0[0] == "rcv":
            if len(queue0) > 0:
                registers0[row0[1]] = queue0.pop()
            else: # no value to receive, stay at same instruction
                pos0 -= 1

        if row0[0] == "jgz":
            if convert_value(row0[1], registers0) > 0:
                pos0 += convert_value(row0[2], registers0) - 1

        pos0 += 1

if __name__ == "__main__":
    filename = "day18_instructions.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        instructions = open(filename).read().split("\n")
        part_1 = recover_frequency(instructions)
        part_2 = concurrent_programs(instructions)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
