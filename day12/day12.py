#!/usr/bin/env python3

import os.path

def programs_reached(neighbors, start_id):
    """Return the list of programs connected to (and including) start_id."""

    already_seen = {start_id}
    to_visit     = set(neighbors[start_id])

    while len(to_visit) > 0:
        next_to_visit = set()
        for node in to_visit:
            already_seen.add(node)
            for next_node in neighbors[node]:
                if next_node not in already_seen and \
                   next_node not in to_visit:
                    next_to_visit.add(next_node)

        to_visit = next_to_visit

    return already_seen

def n_groups(lines):
    """Read each line to build the pipes map, find the number of different
    independent groups (part 2) and number of programs in group 0 (part 1)."""

    # build communication map
    neighbors = {}
    for line in lines:
        line = line.strip().split("<->")
        program = int(line[0])
        neigh = list(map(int, line[1].split(',')))
        neighbors[program] = neigh

    # cell[i] contains the group_id of program with id i
    group_of = [None for _ in range(len(neighbors))]
    group_id = 0

    for i in range(len(neighbors)):
        if group_of[i] is None: # never seen, so use it as starting node
            programs = programs_reached(neighbors, i)
            for prog in programs:
                group_of[prog] = group_id
            group_id += 1 # move to next group

    # find number of programs in group 0
    group0 = [x for x in group_of if x == 0]

    return len(group0), group_id

if __name__ == '__main__':
    filename = "day12_village.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        pipes = open(filename).read().strip().split('\n')
        part_1, part_2 = n_groups(pipes)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
