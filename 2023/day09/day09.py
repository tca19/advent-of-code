#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 9 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where each line is a sequence of numbers. The sequence is
# ordered from left to right, so the "next" value of a number is the number
# immediately at its right.
#
# An example of such file is:
#
#   0 3 6 9 12 15
#   1 3 6 10 15 21
#   10 13 16 21 30 45
#
# For each line, we compute all the differences between one number and the
# "next" number in the sequence. This gives a new sequence of numbers, with one
# less value. We repeat this process until all the differences between numbers
# are 0.
#
# Part 1
# ======
# Once all the values of the sequence are 0, add an additional 0 at the extreme
# right of it. Since this new 0 represents the difference between the last and
# the penultimate numbers at the previous step of the process, we can also add
# an additional number at the extreme right of the sequence at the previous
# step to meet this difference condition. Iterating backward, we can add
# additional numbers at the extreme right up until we add an additional number
# at the extreme right of the original sequence. This new number is called "the
# extrapolated next value". The task is to find the sum of the extrapolated
# values for all lines.
#
# Part 2
# ======
# Instead of adding an additional 0 at the extreme right of the sequence, add
# it at the extreme left of the sequence. Since this new 0 represents the
# difference between the first and the second numbers at the previous step of
# the process, we can also add an additional number at the extreme left of the
# sequence at the previous step to meet this difference condition. Iterating
# backward, we can add additional numbers at the extreme left up until we add
# an additional number at the extreme left of the original sequence (this is
# VERY similar to Part 1, except that you now add new numbers at the extreme
# left of the sequence instead of the extreme right). This new number is called
# "the extrapolated previous value". The task is to find the sum of the
# extrapolated previous values for all lines.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def extrapolate_right(numbers: list[int]) -> int:
    """
    Return the extrapolated next value of the `numbers` sequence.

        Parameters:
            numbers (list[int]): The original sequence of numbers.

        Returns:
            extrapolated (int): The extrapolated number at the extreme right of
                                the original sequence.
    """
    # At each step, the additional value at the extreme right can be called X.
    # We have:
    #     [...] a  X
    #     [...]   b
    #
    # b is the difference between X and a so: X - a = b. Which gives X = a + b.
    # So the extrapolated value X of the original sequence is simply the sum of
    # all extrapolated values at each step, until we have a sequence of 0.
    # The sum is initialized with the last value of the original sequence.
    extrapolated = numbers[-1]
    while not all(x == 0 for x in numbers):
        numbers = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
        extrapolated += numbers[-1]

    return extrapolated


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day09.input")
    args = parser.parse_args()

    # Open the input file, and read it line by line. The, parse each line
    # (sequences of integer numbers).
    with open(args.input, encoding="UTF-8") as f:
        data = [list(map(int, line.split())) for line in f.readlines()]

    part1 = sum(extrapolate_right(sequence) for sequence in data)
    print(f"Part 1: {part1}")

    # Let's illustrate Part 2 with an example sequence. The
    # sequence could look like:
    #
    #     a    b    c    d    (initial sequence)
    #       b-a  c-b  d-c     (first step of differences)
    #
    # Then we add the additional values (X and Y) at the extreme left.
    #
    #    X    a     b      c      d
    #       Y   b-a    c-b    d-c
    #
    # We have: a - X = Y. Therefore, X = a - Y.
    # Let's do Part 1 on the same sequence, but reversed. We have:
    #
    #     d    c    b    a    (initial sequence but reversed)
    #       c-d  b-c  a-b     (first step of differences)
    #
    # Then we add the additional values at the extreme right (Part 1).
    #
    #     d    c    b    a     Z
    #       c-d  b-c  a-b   W
    #
    # We have: Z - a = W. So Z = a + W.
    # Obviously, W = - Y (sequence is reversed, so each difference is the
    # opposite of its corresponding one). So Z = a - Y. Which is the same as X
    # because X = a - Y. So X = Z. In other words, to find the value of X
    # (which is what we are looking for, the extrapolated previous value of the
    # sequence), we simply have to compute the value Z, the extrapolated next
    # value of the reversed sequence.
    part2 = sum(extrapolate_right(sequence[::-1]) for sequence in data)
    print(f"Part 2: {part2}")
