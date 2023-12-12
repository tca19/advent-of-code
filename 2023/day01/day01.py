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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def generate_number(line: str) -> int:
    """
    Generate a 2-digit number by concatenating the first and the last digit
    found in the alphanumeric sequence `line`.

        Parameters:
            line (str): A string, composed of alphanumeric characters.

        Returns:
            number (int): The 2-digit number generated from `line`.
    """
    number = ""
    digits = "123456789"

    # Find first digit
    first_positions = []
    for digit in digits:
        pos = line.find(digit)
        if pos > -1:
            first_positions.append((pos, digit))
    first_positions.sort()
    number += first_positions[0][1]

    # Find last digit
    last_positions = []
    for digit in digits:
        pos = line.rfind(digit)  # rfind() looks for 1st occurence from the end
        if pos > -1:
            last_positions.append((pos, digit))
    last_positions.sort(reverse=True)
    number += last_positions[0][1]

    return int(number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day01.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    part1 = sum(generate_number(line) for line in data)
    print(f"Part 1: {part1}")
