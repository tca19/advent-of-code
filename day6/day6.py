#!/usr/bin/env python3

import os.path

def loop_size(banks):
    """Count number of states required to find an already seen state, and the
    size of the loop."""

    states    = {} # store each state + the step at which we saw it first
    n_state   = 0

    while True:
        # look if we already met this state. If already met, exit the program.
        # else, add the new state and the current step
        representation = ';'.join(list(map(str, banks)))
        if representation in states:
            break
        else:
            states[representation] = n_state

        # find cell index in banks with the most blocks
        i = 0
        for k in range(1, len(banks)):
            if banks[k] > banks[i]:
                i = k

        # redistribute
        blocks_to_give = banks[i]
        banks[i] = 0
        while blocks_to_give > 0:
            i = (i + 1) % len(banks)
            banks[i] += 1
            blocks_to_give -= 1

        n_state += 1

    return n_state, n_state - states[representation]

if __name__ == '__main__':
    filename = "day6_banks.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        banks = list(map(int, open(filename).read().split()))
        part_1, part_2 = loop_size(banks)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
