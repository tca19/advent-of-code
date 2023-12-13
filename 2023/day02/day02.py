#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 2 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where each line represents a game of "drawing colored
# cubes". Each line starts by indicating the ID of the corresponding game.
#
# An example of such file is:
#
#   Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#   Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#   Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#   Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#   Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#
# For each game, we draw a set a colored cubes from a big bag, replace the
# cubes into the bag and repeat this operation several more times. So at the
# end, we draw N sets of cubes. The line indicates the composition of each
# sets, separating them with ";". The cubes are either red, blue or green.
#
# Part 1
# ======
# Let's suppose that the bag of cubes contains:
#    - 12 red cubes
#    - 13 green cubes
#    - 14 blue cubes
# Some games would be impossible because some of the sets have a larger number
# of red (or green, or blue) cubes. The task is to compute the sum of the IDs
# of the games that are possible (and only those games).
#
# Part 2
# ======
# For each game, we need to find the minimum number of red, green and blue
# cubes so that the game is possible (i.e. every drawn set is possible). Then,
# we can compute the "power" of all sets in a game by multiplying the minimum
# number of cubes for all colors. The task is to find the sum of all "power"
# for each game.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse
from collections import defaultdict

# The expected number of cubes in the bag for each color (used in Part 1).
MAX_N_RED, MAX_N_GREEN, MAX_N_BLUE = 12, 13, 14


def parse_line(line: str) -> tuple:
    """
    Parse the line to get info about game ID and each cube sets we drawed.

        Parameters:
            line (str): The line to be parsed.

        Returns:
            infos (tuple): Return the game information as a tuple. First
                           element is the game ID. Second element is a list of
                           cube sets. Each cube sets is a dictionary that
                           indicate the number of respective "red", "blue" and
                           "green" cube it contains.
    """
    game_info, sets_info = line.strip().split(":")
    game_id = int(game_info.split()[1])

    cube_sets = []
    for cube_set in sets_info.split(";"):
        n_cubes = defaultdict(int)
        for cubes in cube_set.split(","):
            n, color = cubes.strip().split()
            n_cubes[color] = int(n)
        cube_sets.append(n_cubes)

    return (game_id, cube_sets)


def is_cube_set_valid(n_cubes: dict) -> bool:
    """
    Indicate if the cube set is valid, given its composition of red/green/blue
    cubes.

        Parameters:
            n_cubes (dict): A dictionary indicating the composition of the cube
                            set. It maps colors (the keys) to their respective
                            number of cubes (the values).

        Returns:
            is_valid (bool): True if the cube set is valid. False otherwise.
    """
    # A "valid" cube set means that for each color, the number of cube is not
    # greater than the total number of cube of this color in the drawing bag.
    if n_cubes["red"] > MAX_N_RED:
        return False
    if n_cubes["green"] > MAX_N_GREEN:
        return False
    if n_cubes["blue"] > MAX_N_BLUE:
        return False
    return True


def compute_game_power(cube_sets: list) -> int:
    """
    Compute the product of minimum red, green and blue cubes we need so that
    every cube sets are valid.

        Parameters:
            cube_sets (list): List of drawn cube sets. Each set is a dictionary
                              indicating the number of red, green and blue
                              cubes.
        Returns:
            power (int): The product of minimum number of red, green and blue
                         cubes.
    """
    min_red, min_green, min_blue = 0, 0, 0
    for cube_set in cube_sets:
        min_red = max(min_red, cube_set["red"])
        min_green = max(min_green, cube_set["green"])
        min_blue = max(min_blue, cube_set["blue"])

    power = min_red * min_green * min_blue
    return power


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day02.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    all_games = [parse_line(line) for line in data]
    possible_games = [game_id for (game_id, cube_sets) in all_games
                      if all(is_cube_set_valid(n_cubes)
                             for n_cubes in cube_sets)]
    part1 = sum(possible_games)
    print(f"Part 1: {part1}")

    all_powers = [compute_game_power(cube_sets)
                  for (game_id, cube_sets) in all_games]
    part2 = sum(all_powers)
    print(f"Part 2: {part2}")
