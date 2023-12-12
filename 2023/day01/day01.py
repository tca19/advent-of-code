#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 1 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where each line is a sequence of alphanumeric characters.
#
# An example of such file is:
#
#   1abc2
#   pqr3stu8vwx
#   a1b2c3d4e5f
#   treb7uchet
#
# Part 1
# ======
# For each line, find the first and the last digits in the alphanumeric
# sequence. Combine these 2 digits to form a 2-digit number. The task is to
# find the sum of all numbers generated for each line.
#
# Part 2
# ======
# Instead of only looking at regular digits (1, 2, ..., 9), we also look at
# spelled digits, which are "one", "two", ... "nine". The task is the same as
# for Part 1, finding the sum of all the generated 2-digits numbers, using the
# first and last digits found on each line.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def generate_number(line: str, use_spelled_digits: bool = False) -> int:
    """
    Generate a 2-digit number by concatenating the first and the last digit
    found in the alphanumeric sequence `line`. Either use the regular digits
    (1, 2, ..., 9) and/or the spelled digits ("one", "two", ..., "nine").

        Parameters:
            line (str): A string, composed of alphanumeric characters.
            use_spelled_digits (bool): Indicates if we need to use the spelled
                                       digits to find first and last digits.

        Returns:
            number (int): The 2-digit number generated from `line`.
    """
    number = ""
    digits = list("123456789")
    if use_spelled_digits:
        digits += ["one", "two", "three", "four", "five", "six", "seven",
                   "eight", "nine"]

    # Find first digit
    first_positions = []
    for i, digit in enumerate(digits):
        pos = line.find(digit)
        if pos > -1:
            # (i%9) + 1 is the value of the digit we just found. I need to do
            # it this way to translate "one" to 1, "two" to 2, "nine" to 9 ...
            first_positions.append((pos, (i % 9) + 1))
    first_positions.sort()
    number += str(first_positions[0][1])

    # Find last digit
    last_positions = []
    for i, digit in enumerate(digits):
        pos = line.rfind(digit)  # rfind() looks for 1st occurence from the end
        if pos > -1:
            # (i%9) + 1 is the value of the digit we just found. I need to do
            # it this way to translate "one" to 1, "two" to 2, "nine" to 9 ...
            last_positions.append((pos, (i % 9) + 1))
    last_positions.sort(reverse=True)
    number += str(last_positions[0][1])

    return int(number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day01.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    part1 = sum(generate_number(line, use_spelled_digits=False)
                for line in data)
    print(f"Part 1: {part1}")

    part2 = sum(generate_number(line, use_spelled_digits=True)
                for line in data)
    print(f"Part 2: {part2}")
