#!/usr/bin/env python3

import os.path

def programs_dance(moves, programs):
    """Make the programs dance according to the moves sequence. Return the list
    of programs after the dance."""

    for move in moves:
        if move[0] == "s":
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]
        if move[0] == "x":
            A, B = move[1:].split("/")
            A, B = int(A), int(B)
            programs[A], programs[B] = programs[B], programs[A]
        if move[0] == "p":
            A, B = move[1:].split("/")
            A, B = programs.index(A), programs.index(B)
            programs[A], programs[B] = programs[B], programs[A]

    return "".join(programs)

def programs_dance_repeat(moves):
    """Find the programs order after 1 billion dances."""

    # the dance is a permutation of all programs (because we end up with a list
    # of 16 elements containing "a", "b", ... "p" in different order).
    # Everytime we repeat the dance, we repeat the same permutation. Landau has
    # proved that recursively applying the same permutation a certain number
    # of times (named orbit) makes the sequence returns to its original state.
    # For a sequence of 16 elements, the maximum possible length of this cycle
    # is 140 (https://oeis.org/A000793). So we start by computing the length of
    # the cycle of our permutation.
    original = "abcdefghijklmnop"
    programs = original[:]
    len_cycle = 0

    while True: # at most 140 iterations => no infinite loop
        programs   = programs_dance(moves, list(programs))
        len_cycle += 1
        if programs == original:
            break

    # then, we only need to repeat the dance for (10^9 % len_cycle) to know the
    # state after 1 billion dance.
    for _ in range(10**9 % len_cycle):
        programs = programs_dance(moves, list(programs))

    return programs

if __name__ == '__main__':
    filename = "day16_dance.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        moves = open(filename).read().strip().split(',')
        part_1 = programs_dance(moves, list("abcdefghijklmnop"))
        print("PART ONE:", part_1)
        part_2 = programs_dance_repeat(moves)
        print("PART TWO:", part_2)
