#!/usr/bin/env python3

import os.path
from collections import defaultdict

def process_instructions(instructions):
    """For each instructions, increase or decrease value of register. Return the
    maxi value of all registers, and the max value held during process."""

    # defaultdict so not seen registers have value of 0 (as required)
    registers    = defaultdict(int)
    max_held_val = 0

    for instruction in instructions:
        name, cmd, val, _, op1, op, op2 = instruction.split()

        if op == ">":
            condition = registers[op1] > int(op2)
        elif op == "<":
            condition = registers[op1] < int(op2)
        elif op == ">=":
            condition = registers[op1] >= int(op2)
        elif op == "<=":
            condition = registers[op1] <= int(op2)
        elif op == "==":
            condition = registers[op1] == int(op2)
        elif op == "!=":
            condition = registers[op1] != int(op2)

        if condition:
            if cmd == "inc":
                registers[name] += int(val)
            else:
                registers[name] -= int(val)

        max_held_val = max(max_held_val, registers[name])

    max_val = max(registers.values())
    return max_val, max_held_val

if __name__ == '__main__':
    filename = "day8_instructions.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        instructions = open(filename).read().strip().split("\n")
        part_1, part_2 = process_instructions(instructions)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
