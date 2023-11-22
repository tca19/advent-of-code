#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 3 in Advent of Code 2022.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where lines are long string of uppercase/lowercase
# letters.
#
# An example of such file is:
#
#   vJrwpWtwJgWrhcsFMMfFFhFp
#   jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#   PmmdzqPrVvPwwTWBwg
#   wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#   ttgJtRGJQctTZtZT
#   CrZsJsPPZsGzwwsLwLmpwMDw
#
# Each letter (like 'a', 'b', 'L', ...) represents an item and each line
# represents a rucksack (so a rucksack contains many items). Each rucksack is
# split into 2 compartments. They both have same size: the first half of the
# string represents items in the first compartment, while the second half of
# the string represents the items in the second compartment.
#
# Part 1
# ======
# For each rucksack, find the single item that appears in both compartments.
# Assign it a priority value (lowercase item types 'a' through 'z' have
# priorities 1 through 26, uppercase item types 'A' through 'Z' have priorities
# 27 through 52).
#
# The task is to find the sum of the priorities of those items.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# We open the input file, and read it line by line
with open("day03.input", encoding="UTF-8") as f:
    data = f.read().splitlines()


def compute_priority(item: str) -> int:
    """
    Return the priority value of the item, given the rule stated in the
    challenge description.

        Parameters:
            item (str): the item. A single letter.

        Returns:
            priority (int): the priority of the item.
    """
    priority = None
    if item.islower():
        priority = ord(item) - ord('a') + 1
    else:
        priority = ord(item) - ord('A') + 27

    return priority


def solve_part1(rucksacks: list[str]) -> int:
    """
    Return the sum of priorities of items that are in both compartments of each
    rucksack.

        Parameters:
            rucksacks (list[str]): the list of rucksacks. Each rucksack is a
                                   string.

        Returns:
            sum_priorities (int): the sum of priorities.
    """
    sum_priorities = 0
    for rucksack in rucksacks:
        # Split rucksack in 2 compartments.
        middle = len(rucksack) // 2  # // for an integer division, not float
        compartment1, compartment2 = rucksack[:middle], rucksack[middle:]

        # Find the common element. Use [ ] to extract the single element.
        [common_item] = set(compartment1) & set(compartment2)
        sum_priorities += compute_priority(common_item)

    return sum_priorities


if __name__ == "__main__":
    part1 = solve_part1(data)

    print(f"Part 1: {part1}")
