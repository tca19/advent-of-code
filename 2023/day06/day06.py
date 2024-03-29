#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 6 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file that contains only two lines. An example of such file is:
#
#   Time:      7  15   30
#   Distance:  9  40  200
#
# This file has to be read column by column. It represents boat races. For the
# first race, the time is 7 milliseconds and the record distance is 9
# millimeters.  The objective is to participate in this race and beat the
# distance record.  For each race, we have a time limit (indicated by the first
# line). During this time, we can charge our boat (this increases its speed) or
# start to race and go at that speed during the time left. Each milliseconds
# we spend to charge the boat increases its speed by 1 millimeters per
# milliseconds.

# So for the first race, if we charge the boat for 4 milliseconds and then go,
# its speed is 4 millimeters per milliseconds and we travel 4 * 3 (time left) =
# 12 millimeters. Therefore, we beat the distance record (because 12 > 9). We
# can choose for how long we charge the boat, but it will influence (for better
# or for worse) the distance traveled.
#
# Part 1
# ======
# For each race, count how many ways there exist to beat the distance record.
# The task is to find the product of all the number of ways for each race.
#
# Part 2
# ======
# Now, there is only a single race instead of several ones! The time limit for
# this single race is obtained by concatenating the numbers on the "Time:"
# line. The distance record is also obtained by concatenating the numbers on
# the "Distance:" line. For the example file, this gives a time limit of 71530
# and a distance record of 940200. The task is to find how many ways there
# exist to beat the distance record on this single race.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def n_ways_beat_record(time_limit: int, distance_record: int) -> int:
    """
    Return the number of ways to beat the `distance_record` of the race, given
    the `time_limit`.

        Parameters:
            time_limit (int): The time limit of the race. We need to charge and
                              travel only during this time limit.
            distance_record (int): The distance we have to beat.

        Returns:
            n_ways (int): The number of ways to beat the distance record.
    """
    n_ways = 0
    # Do not consider the extreme cases:
    #   - hold_time = 0 (means speed = 0, and therefore traveled_distance = 0)
    #   - hold_time = time_limit (means time_left = 0, and therefore
    #                             traveled_distance = 0)
    for hold_time in range(1, time_limit):
        speed = hold_time  # speed increases by 1 for each milliseconds held
        time_left = time_limit - hold_time
        traveled_distance = speed * time_left
        if traveled_distance > distance_record:
            n_ways += 1
    return n_ways


def n_ways_beat_record_optimized(time_limit: int, distance_record: int) -> int:
    """
    Return the number of ways to beat the `distance_record` of the race, given
    the `time_limit`. Use the mathematical formula instead of ranging over all
    possible choices.

        Parameters:
            time_limit (int): The time limit of the race. We need to charge and
                              travel only during this time limit.
            distance_record (int): The distance we have to beat.

        Returns:
            n_ways (int): The number of ways to beat the distance record.
    """
    # Let's denote the holding time as X. We have:
    #           speed = hold_time = X
    # and       time_left = time_limit - hold_time = time_limit - X
    # Therefore:
    #           traveled_distance = speed * time_left
    #                             = X * (time_limit - X)
    #                             = -X^2 + X * time_limit
    # We search the values X such that traveled_distance > distance_record.
    # Which is:
    #           -X^2 + X * time_limit > distance_record
    # i.e.      -X^2 + X * time_limit - distance_record > 0
    #
    # We have a polynom of degree 2 with a negative coefficient for X^2. The
    # values of X that meet the inequality criteria are between the roots of
    # the polynom P = -X^2 + X * time_limit - distance_record
    delta = time_limit * time_limit - 4 * (-1) * (-distance_record)
    root1 = (1/2) * (-time_limit - delta**0.5)
    root2 = (1/2) * (-time_limit + delta**0.5)
    min_valid_x = int(root1) + 1
    max_valid_x = int(root2)
    return max_valid_x - min_valid_x + 1


def product(values: list[int]) -> int:
    """
    Return the product of all values in `values`.

        Parameters:
            values (list[int]): The list of values.

        Returns:
            prod (int): The product of all elements.
    """
    prod = 1
    for v in values:
        prod *= v
    return prod


if __name__ == "__main__":
    # pylint: disable=C0103
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day06.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    times_str = data[0].split(":")[1].split()
    times = list(map(int, times_str))
    distances_str = data[1].split(":")[1].split()
    distances = list(map(int, distances_str))

    part1 = product([n_ways_beat_record_optimized(t, d)
                     for (t, d) in zip(times, distances)])
    print(f"Part 1: {part1}")

    time_single_race = int("".join(times_str))
    distance_single_race = int("".join(distances_str))
    part2 = n_ways_beat_record_optimized(time_single_race,
                                         distance_single_race)
    print(f"Part 2: {part2}")
