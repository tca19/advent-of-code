#!/usr/bin/env python3

import os.path
from collections import defaultdict

def process_instructions(instructions):
    """For each instruction, increase or decrease value of register. Return the
    largest value of all registers, and the max value held during process."""

    registers    = defaultdict(int)
    max_held_val = 0

    for instruction in instructions:
        name, cmd, val, _, op1, op, op2 = instruction.split()

        condition = eval("{} {} {}".format(registers[op1], op, op2))

        if condition:
            if cmd == "inc":
                registers[name] += int(val)
            else:
                registers[name] -= int(val)

        max_held_val = max(max_held_val, registers[name])

    return max(registers.values()), max_held_val

if __name__ == '__main__':
    filename = "day08_instructions.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        instructions = open(filename).read().strip().split("\n")
        part_1, part_2 = process_instructions(instructions)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
