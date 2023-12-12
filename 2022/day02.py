#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 2 in Advent of Code 2022.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file where each line represents a round of the game "Rock,
# Paper, Scissors". Each line has 2 letters:
#   - the first letter is A, B or C. It is the choice of my opponent.
#   - the second letter is X, Y or Z. It is my choice.
#
# An example of such file is:
#
#    A Y
#    B X
#    C Z
#
# The letter A represents Rock, B represents Paper and C represents Scissors.
#
# Part 1
# ======
# Let's suppose that X represents Rock, Y represents Paper and Z represents
# Scissors. Let's also suppose that Rock has a score of 1, Paper a score of 2
# and Scissors a value of 3. Let's also suppose that if I win the round, I get
# a score of 6, a score of 3 if the round is a draw and a score of 0 if I
# loose the round. So if I win a round by playing Paper, I get a score of 8:
#   6 (because I win) + 2 (because I play Paper) = 8
#
# The task is to calculate my total score after playing all rounds.
#
# Part 2
# ======
# This time, the letters X, Y and Z do not represent my choice, but the
# expected outcome of the round: X means a Lose, Y a Draw and Z a Win. For each
# round, I have to find the appropriate choice that ends the round with the
# expected outcome. Then compute the score the same way as for part 1.
#
# The task is to calculate my total score after playing all rounds, with the
# new constraint given by the expected outcome of each round.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# We open the input file, and read it line by line (i.e. round after round).
with open("day02.input", encoding="UTF-8") as f:
    data = f.read().splitlines()

# For easier readability, let's convert the letters to what they represent.
letter_to_choice = {
    "A": "Rock", "B": "Paper", "C": "Scissors",
    "X": "Rock", "Y": "Paper", "Z": "Scissors"
}

# We can also create a score table for: the choice made + the outcome of the
# round.
score = {
    "Rock": 1, "Paper": 2, "Scissors": 3,
    "Win": 6,  "Draw":  3, "Lose": 0
}

# Now we can generate an outcome table. Since there are only 9 different
# possible games, we can determine for each one of them if it ends with a Win,
# a Draw or a Lose. Let's assume that my choice is the second element in each
# (a,b).
round_outcome = {
    ("Rock",     "Rock"):     "Draw",
    ("Rock",     "Paper"):    "Win",
    ("Rock",     "Scissors"): "Lose",
    ("Paper",    "Rock"):     "Lose",
    ("Paper",    "Paper"):    "Draw",
    ("Paper",    "Scissors"): "Win",
    ("Scissors", "Rock"):     "Win",
    ("Scissors", "Paper"):    "Lose",
    ("Scissors", "Scissors"): "Draw",
}


def score_part1(list_rounds: list[str]) -> int:
    """
    Return the total score after playing each round.

        Parameters:
            list_rounds (list[str]): A list of rounds. A round is a string
                                     composed of 2 letters, separated by a
                                     space.
        Returns:
            total_score (int): The sum of all my scores obtained after each
                               round.
    """
    total_score = 0
    for round_letters in list_rounds:
        # Get the choice of each player, by converting the letter to the
        # choice.
        opponent_letter, my_letter = round_letters.split()
        opponent_choice = letter_to_choice[opponent_letter]
        my_choice = letter_to_choice[my_letter]

        # Get the outcome of the round, to compute my score.
        outcome = round_outcome[(opponent_choice, my_choice)]
        score_round = score[my_choice] + score[outcome]
        total_score += score_round
    return total_score


def score_part2(list_rounds: list[str]) -> int:
    """
    Return the total score after playing each round, with the new constraint
    given by the expected outcome of each round.

        Parameters:
            list_rounds (list[str]): A list of rounds. A round is a string
                                     composed of 2 letters, separated by a
                                     space.
        Returns:
            total_score (int): The sum of all my scores obtained after each
                               round.
    """
    expected_outcome = {
        "X": "Lose", "Y": "Draw", "Z": "Win"
    }
    total_score = 0
    for round_letters in list_rounds:
        opponent_letter, expected_letter = round_letters.split()
        opponent_choice = letter_to_choice[opponent_letter]
        outcome = expected_outcome[expected_letter]

        # To find my choice, we iterate over all possible game combinations and
        # select the one that has: the same opponent choice + the correct
        # expected output.
        for (opp, mine), out in round_outcome.items():
            if opp == opponent_choice and out == outcome:
                my_choice = mine
                break

        score_round = score[my_choice] + score[outcome]
        total_score += score_round
    return total_score


if __name__ == "__main__":
    part1 = score_part1(data)
    part2 = score_part2(data)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
