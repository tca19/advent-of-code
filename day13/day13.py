#!/usr/bin/env python3

import os.path
from collections import defaultdict

def create_lengths(lines):
    """Read lines to create a list of layers length."""

    layers   = defaultdict(int)

    # get the length of all layers (from lines)
    for line in lines:
        line = list(map(int, line.split(":")))
        layers[line[0]] = line[1]

    # create list representing layers length. Set 0 if there is no layer at
    # depth i (because of defaultdict)
    max_depth = max(layers.keys())
    lengths = [layers[depth] for depth in range(max_depth+1)]

    return lengths

def compute_severity(lengths):
    """Compute the severity of the trip across all layers."""

    # for each layer, we only care if the scanner is in position 0 (because the
    # packet will get caught only if scanner is in position 0). The scanner
    # follows a cycle and position 0 is reached every 2*(n-1) steps where n is
    # the layer length (because traversing the layer takes n-1 steps and coming
    # back at 0 needs 2 traversal). So we check if the packet arrives at the
    # same moment as the scanner.
    severity = 0
    for depth in range(len(lengths)):
        if lengths[depth] == 0: # no layer, can't get caught
            continue
        if depth % (2 * (lengths[depth] - 1)) == 0:
            severity += depth * lengths[depth]

    return severity

def find_delay(lengths):
    """Find the delay required to not get caught."""

    # bruteforce: test all delays until finding the right one. We stop when the
    # packet can traverse all layers without getting caught.
    delay = 0
    while True:
        caught = False
        for depth in range(len(lengths)):
            if lengths[depth] == 0:
                continue
            if (depth+delay) % (2 * (lengths[depth] - 1)) == 0:
                caught = True
                break

        if not caught:
            break

        delay += 1

    return delay

if __name__ == '__main__':
    filename = "day13_firewall.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lengths = create_lengths(open(filename).read().strip().split("\n"))
        part_1 = compute_severity(lengths)
        print("PART ONE:", part_1)
        part_2 = find_delay(lengths)
        print("PART TWO:", part_2)
