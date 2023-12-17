#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 5 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file, composed of several sections that indicate how to map
# various things to other various things.
#
# An example of such file is:
#
#   seeds: 79 14 55 13
#
#   seed-to-soil map:
#   50 98 2
#   52 50 48
#
#   soil-to-fertilizer map:
#   0 15 37
#   37 52 2
#   39 0 15
#
#   fertilizer-to-water map:
#   49 53 8
#   0 11 42
#   42 0 7
#   57 7 4
#
# There are other sections that follow the same pattern after this:
#    - water-to-light map:
#    - light-to-temperature map:
#    - temperature-to-humidity map:
#    - humidity-to-location map:
#
# The first line indicates the IDs of seeds we have. Then, for each section, we
# have lines that follow this pattern: destination range start, source range
# start, range length. For the "seed to soil" mapping, we have for example this
# line: 50 98 2. It means that seeds with IDs in [98, 99] (because source start
# is 98 and range length is 2) are mapped to soils in [50, 51]. All seeds with
# an ID not in [98, 99] are mapped to a soil with the same ID.
#
# Part 1
# ======
# Follow all needed transformations to map a seed to its final location (i.e.
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity ->
# location). Repeat the process for all seeds. The task is to find the lowest
# location that corresponds to any of the initial seeds.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def apply_mapping(source: int, ranges: list) -> int:
    """
    Apply the mapping rules to transform the `source` value. Return the
    computed new `value`.

        Parameters:
            source (int): The ID of the object we want to map.
            ranges (list): The list of all mapping ranges we know for this
                           transformation. Each mapping is a string like:
                           destination start, source start, range length

        Returns:
            result (int): The value of the source ID after applying the
                          appropriate mappping range. Returns the source ID if
                          no compatible mapping has been found.
    """
    for range_ in ranges:
        dst_start, src_start, length = list(map(int, range_.split()))
        if src_start <= source <= (src_start + length-1):
            offset = source - src_start
            result = dst_start + offset
            return result
    return source  # no compatible mapping range found, return source ID.


def apply_consecutive_mappings(source: int, mappings: list) -> int:
    """
    Apply all the consecutive mapping rules to transform the `source` value
    into its final location value. Return the computed final `location`.

        Parameters:
            source (int): The ID of the object we want to map.
            mappings (list): The list of all consecutive mappings ranges we
                             know for each transformation.

        Returns:
            location (int): The value of the location ID after applying all the
                            consecutive appropriate mappping ranges.
    """
    for mapping in mappings:
        source = apply_mapping(source, mapping)
    return source  # variable is called "source" but it's the final location.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day05.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.read().split("\n\n")

    # Parse input data to get seeds ID.
    seeds_str = data[0].split(":")[1]
    seeds = tuple(map(int, seeds_str.split()))

    # Parse input data to get all the mappings.
    all_mappings = []
    for block in data[1:]:
        # first line (.split("\n")[0]) is useless. It's the mapping's name.
        mapping_ranges = block.strip().split("\n")[1:]
        all_mappings.append(mapping_ranges)


    locations = [apply_consecutive_mappings(seed, all_mappings)
                 for seed in seeds]
    part1 = min(locations)
    print(f"Part 1: {part1}")
