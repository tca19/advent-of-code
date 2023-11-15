#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 1 in Advent of Code 2022.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where lines are either:
#   - a single integer
#   - a blank line
#
# An example of such file is:
#
#   1000
#   2000
#   3000
#
#   4000
#
#   5000
#   6000
#
#   7000
#   8000
#   9000
#
#   10000
#
# We can see that the integers form groups (separated by an empty line). In
# this example, the first group is composed of 1000, 2000 and 3000. The sum of
# all integers in this group is 6000.
#
# Part 1
# ======
# The task is to find the group with the largest sum, and to print this sum.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# We open the input file, and instead of reading it line by line, we read it
# "group" by "group" (since we know that each group is separated by an empty
# line, i.e. a double \n)
with open("day01.input", encoding="UTF-8") as f:
    data = f.read().split("\n\n")


def sum_group(group: str) -> int:
    """
    Return the sum of all integers in `group`.

        Parameters:
            group (str): A string, composed of one or more lines. Each line is
                         a single integer.
        Returns:
            group_sum (int): The sum of all integers in the group
    """
    values = [int(number) for number in group.strip().split("\n")]
    return sum(values)


if __name__ == "__main__":
    group_sums = [sum_group(group) for group in data]
    part1 = max(group_sums)

    print(f"Part 1: {part1}")
