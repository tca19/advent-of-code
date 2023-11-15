#!/usr/bin/env python3

import os.path

def parse_file(filename):
    """Read each line as a tuple of integers. Return a set of these tuples."""

    components = set()
    with open(filename) as f:
        for line in f:
            p1, p2 = list(map(int, line.split("/")))
            components.add((p1, p2))

    return components

def max_strength_bridge(port, components, strength, length=None):
    """Build all possible bridges with available components starting with the
    same number of pin as port. Return the one with the maximum strength, or the
    one with maximum length."""

    # find components that can be connected to port
    candidates = [c for c in components if port in c]

    # no candidate, cannot append another component to the bridge. return
    # current length and strength
    if len(candidates) == 0:
        return (length, strength)

    # for each candidate, remove it from the list of available components and
    # find the maximum strength we can build if we continue the same process.
    # return the maximum strength among all possible strength
    possible_strength = []
    for c in candidates:
        new_port = c[1] if c[0] == port else c[0]
        new_components = set(components) # copy because .remove() done in place
        new_components.remove(c)
        possible_strength.append(max_strength_bridge(new_port, new_components,
            strength + sum(c), None if length is None else length+1))

    return max(possible_strength)

if __name__ == "__main__":
    filename = "day24_ports.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        components = parse_file(filename)
        part_1 = max_strength_bridge(0, components, 0, None)[1]
        print("PART ONE:", part_1)
        part_2 = max_strength_bridge(0, components, 0, 0)[1]
        print("PART TWO:", part_2)
