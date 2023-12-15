#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 4 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file representing a list of bingo games. Each line represents
# a bingo card, with the winning numbers and my numbers.
#
# An example of such file is:
#
#   Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#   Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#   Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#   Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#   Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#   Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#
# In the first line, the winning numbers are on the left of the '|' symbol.
# They are: 41, 48, 83, 86 and 17. My numbers are on the right of the '|'
# symbol.
#
# Part 1
# ======
# For each game, we can compute a score based on the count of the numbers that
# I have that are also winning numbers. If I have only 1 winning number, the
# score is 1; 2 wining numbers gives a score of 2; 3 winning numbers gives a
# score of 4; (the score is doubled for each additional winning number). The
# task is to find my total score for all games.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse


def compute_score(n_winning_numbers: int) -> int:
    """
    Return the score of a game given the number of winning numbers.

        Parameters:
            n_winning_numbers (int): The number of winning numbers I have for
                                     this game.

        Returns:
            score (int): The score of the game.
    """
    if n_winning_numbers == 0:
        return 0
    score = 1
    for _ in range(1, n_winning_numbers):
        score *= 2
    return score


def count_winning_numbers(line: str) -> int:
    """
    Return the count of "my numbers" that are also "winning numbers" in the
    game described by `line`.

        Parameters:
            line (str): The string that describes a game. It comes directly from
                        the input file.

        Returns:
            n_winning_numbers (int): The count of my numbers that are also
                                     winning numbers.
    """
    # `line` is like:
    #  Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    _, numbers = line.split(":")
    winning_numbers_str, my_numbers_str = numbers.split(" | ")
    winning_numbers = set(map(int, winning_numbers_str.split()))
    my_numbers = set(map(int, my_numbers_str.split()))

    return len(winning_numbers & my_numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day04.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    part1 = sum(compute_score(count_winning_numbers(line)) for line in data)
    print(f"Part 1: {part1}")
