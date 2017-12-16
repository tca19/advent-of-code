#!/usr/bin/env python3

import os.path

def compute_severity(lines):
    """Compute the severity of the trip across all layers."""

    infos    = {}
    severity = 0

    # get the length of all layers
    for line in layers:
        line = line.split(":")
        infos[int(line[0])] = int(line[1])

    # we are going to iterate on each layer, including empty ones. Regroup the
    # range infos into a list (faster to iterate than a dictionary)
    max_depth = max(infos.keys()) + 1
    lengths = [infos[k] if k in infos else 0 for k in range(max_depth)]

    # for each layer, we only care if the scanner is in position 0 (because the
    # packet will get caught only if scanner is in position 0). The scanner
    # follows a cycle and position 0 is reached every 2*(n-1) steps where n is
    # the length (because traversing the list takes n-1 steps and comming back
    # at 0 needs 2 traversal). So we check if the packet arrives at the same
    # moment.
    for depth in range(max_depth):
        if lengths[depth] == 0: # no layer, can't get caught
            continue
        if depth % (2 * (lengths[depth] - 1)) == 0:
            severity += depth * lengths[depth]

    return severity

def find_delay(layers):
    """Find the delay required to not get caught."""

    infos    = {}

    # get the length of all layers
    for line in layers:
        line = line.split(":")
        infos[int(line[0])] = int(line[1])

    # we are going to iterate on each layer, including empty ones. Regroup the
    # range infos into a list (faster to iterate than a dictionary)
    max_depth = max(infos.keys()) + 1
    lengths = [infos[k] if k in infos else 0 for k in range(max_depth)]

    # bruteforce: test all delays until finding the right one. We stop when the
    # packet can traverse all layers without getting caught. To know how to know
    # if packet get caught at a certain layer, refer to comments in function
    # compute_severity().
    delay = 0

    while True:
        caught = False
        for depth in range(max_depth):
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
        layers = open(filename).read().strip().split("\n")
        part_1 = compute_severity(layers)
        part_2 = find_delay(layers)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
