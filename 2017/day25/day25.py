#!/usr/bin/env python3

import os.path

def perform_turing(n_steps):
    """Follow the instructions on the Turing machine blueprint. Return the
    number of 1 after n_steps iterations."""

    tape  = [0 for _ in range(10001)]
    pos   = 5000
    state = "A"

    for _ in range(n_steps):
        if state == "A":
            state = "BF"[tape[pos]]
            pos, pos_ = pos + 1 - 2*tape[pos], pos
            tape[pos_] ^= 1
        elif state == "B":
            state = "CD"[tape[pos]]
            tape[pos] = 0
            pos += 1
        elif state == "C":
            state = "DE"[tape[pos]]
            pos, pos_ = pos - 1 + 2*tape[pos], pos
            tape[pos_] = 1
        elif state == "D":
            state = "ED"[tape[pos]]
            tape[pos] = 0
            pos -= 1
        elif state == "E":
            state = "AC"[tape[pos]]
            pos += 1
        else:
            state = "A"
            pos, pos_ = pos - 1 + 2*tape[pos], pos
            tape[pos_] = 1

    return sum(tape)

if __name__ == "__main__":
    filename = "day25_blueprint.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        n_steps = int(open(filename).read().split("\n")[1].split()[-2])
        part_1 = perform_turing(n_steps)
        print("PART ONE:", part_1)
