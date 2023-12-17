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
#
# Part 2
# ======
# The first line now represents ranges of seeds instead of individual seeds.
# For the values: "79 14 55 13", they are split in groups of 2: (79, 14) and
# (55, 13). The first value in a group is the start of the range. The second
# value is the length of the range. So for the group (79, 14), it corresponds
# to the range [79, 80, 81, ..., 90, 91, 92] (it contains 14 values).  Repeat
# the same process as in Part 1 (to transform a seed to its final location) for
# every seeds in every ranges. The task is to find the lowest location that
# corresponds to any of the seed from the original ranges.
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
    for rule in mappings:
        source = apply_mapping(source, rule)
    return source  # variable is called "source" but it's the final location.


def interval_overlap(interval1: list, interval2: list) -> list:
    """
    Return the overlapping interval between `interval1` and `interval2`.

        Parameters:
            interval1 (list): A list of 2 values indicating the start and end
                              values of first interval.
            interval2 (list): A list of 2 values indicating the start and end
                              values of second interval.

        Returns:
            overlap (list): A list of 2 values indicating the start and end
                            values of the overlapping interval.
    """
    start1, end1 = interval1
    start2, end2 = interval2
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    return [overlap_start, overlap_end]


def apply_mapping_to_ranges(source_ranges: list, mapping_ranges: list) -> list:
    """
    Apply the mapping rules to transform the `source_ranges` into a list of
    transformed ranges. Return the computed new transformed ranges.

        Parameters:
            source_ranges (list): A list of ranges we need to transform given
                                  the mapping rules. Each ranges is like [s,e]
                                  with a start value and an end value.

            mapping_ranges (list): The list of all mapping ranges we know for
                                   this transformation. Each mapping is a
                                   string like: "destination start,
                                   source start, range length".

        Returns:
            transformed_ranges (list): The list of range values after we
                                       applied each mapping to the list of
                                       source ranges.
    """
    transformed_ranges = []
    for source_range in source_ranges:
        overlaps = []
        for range_ in mapping_ranges:
            dst_start, src_start, length = list(map(int, range_.split()))
            overlap = interval_overlap(source_range,
                                       [src_start, src_start + length])
            overlap_length = overlap[1] - overlap[0]
            if overlap_length > 0:
                overlaps.append(overlap)
                offset = overlap[0] - src_start
                # Add the transformed overlap interval.
                transformed_ranges.append(
                    [dst_start + offset, dst_start + offset + overlap_length])

        # We found the ranges of seeds that are transformed with any of the
        # mapping rules. But all the seeds left need to be mapped to
        # themselve (because no mapping rules apply). To find the unmapped
        # seeds, we start by sorting the overlap interval we found (they
        # correspond to seeds that are mapped) and computed the "unmapped"
        # seed ranges with this info. We add them to the `transformed_ranges`,
        # although they are unmapped.
        if len(overlaps) == 0:
            transformed_ranges.append(source_range)
            continue
        overlaps.sort(key=lambda interval: interval[0])
        if source_range[0] < overlaps[0][0]:
            transformed_ranges.append([source_range[0], overlaps[0][0]])
        for i in range(1, len(overlaps)):
            # Special case: two consecutive overlap intervals are "touching"
            # each other (no gap between them). Can't create an "unmapped"
            # interval between them.
            if overlaps[i-1][1] == overlaps[i][0]:
                continue
            start_unmapped = overlaps[i-1][1] + 1
            end_unmapped = overlaps[i][0] - 1
            if start_unmapped < end_unmapped:
                transformed_ranges.append([start_unmapped, end_unmapped])
        if source_range[1] > overlaps[-1][1]:
            transformed_ranges.append([overlaps[-1][1], source_range[1]])

    return transformed_ranges


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
        mapping_rules = block.strip().split("\n")[1:]
        all_mappings.append(mapping_rules)

    locations = [apply_consecutive_mappings(seed, all_mappings)
                 for seed in seeds]
    part1 = min(locations)
    print(f"Part 1: {part1}")

    seed_ranges = []
    for pos in range(0, len(seeds), 2):
        seed_ranges.append([seeds[pos], seeds[pos] + seeds[pos+1]])
    for mapping in all_mappings:
        seed_ranges = apply_mapping_to_ranges(seed_ranges, mapping)
        seed_ranges.sort()
    part2 = min(start_range for (start_range, end_range) in seed_ranges)
    print(f"Part 2: {part2}")
