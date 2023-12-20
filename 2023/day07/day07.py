#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 7 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file that contains poker hands and the bid associated to each
# one of them. A poker hand is a sequence of 5 alphanumeric characters that
# represent the cards we have. Cards can be: A, K, Q, J, T, 9, 8, 7, 6, 5, 4,
# 3, or 2. An example of such file is:
#
#   32T3K 765
#   T55J5 684
#   KK677 28
#   KTJJT 220
#   QQQJA 483
#
# Each poker hand has a type. It can be one of the following 7 types:
#   7 - Five of a kind (AAAAA)
#   6 - Four of a kind (AA8AA)
#   5 - Full house (23332)
#   4 - Three of a kind (TTT98)
#   3 - Two pairs (23432)
#   2 - One pair (A23A4)
#   1 - High card (23456)
#
# Sort all the hands by ascending values. The value of a hand is determined by
# its type ("Five of a kind" is stronger than "Four of a kind", which is
# stronger than "Full house" ...). If two hands have the same type, they are
# sorted by the value of their cards, in the order in their respective hand,
# which means we start by comparing the first card in each hand. If it's the
# same card, we compare the second card. Then the third card ... The rank of a
# card is given by: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3 and 2 ("A" is stronger
# than "K", which is stronger than "Q", which is stronger than "J" ...)

# Part 1
# ======
# Sort the hands in ascending order to find the rank of each hand. The task is
# to compute the product "bid" * "rank" for each hand, then find the total sum
# of these products.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse
from collections import Counter


def get_hand_type(hand: str) -> int:
    """
    Return the type of the poker `hand`. The hand is a sequence of 5
    alphanumeric characters.

        Parameters:
            hand (str): The poker hand. It contains 5 cards (i.e. 5
                        characters).

        Returns:
            hand_type (int): The type of the hand. It ranges from 7 (Five of a
                             kind) to 1 (High card).
    """
    cards_count = [v for k, v in Counter(hand).items()]
    cards_count.sort(reverse=True)  # reverse=True to have host common first

    if len(cards_count) == 1:    # Five of a kind
        hand_type = 7

    elif len(cards_count) == 2:
        if cards_count[0] == 4:  # Four of a kind
            hand_type = 6
        if cards_count[0] == 3:  # Full house
            hand_type = 5

    elif len(cards_count) == 3:
        if cards_count[0] == 3:  # Three of a kind
            hand_type = 4
        if cards_count[0] == 2:  # Two pairs
            hand_type = 3

    elif len(cards_count) == 4:
        if cards_count[0] == 2:  # One pair
            hand_type = 2

    else:  # High card
        hand_type = 1

    return hand_type


def compute_hand_value(hand: str) -> tuple:
    """
    Return a tuple that can be used to sort the poker hands. The tuple contains
    information about the hand type, and the value of each individual cards.

        Parameters:
            hand (str): The poker hand. It contains 5 cards (i.e. 5
                        characters).

        Returns:
            hand_value (tuple): A 6-tuple. It contains the hand type + the
                                value of the 5 cards of the hand.
    """
    cards = "AKQJT98765432"
    card2value = {card: i for i, card in enumerate(cards[::-1])}

    hand_value = (
        get_hand_type(hand),
        card2value[hand[0]],
        card2value[hand[1]],
        card2value[hand[2]],
        card2value[hand[3]],
        card2value[hand[4]]
    )

    return hand_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day07.input")
    args = parser.parse_args()

    # We open the input file, and read it line by line.
    with open(args.input, encoding="UTF-8") as f:
        data = f.readlines()

    poker_hands = []
    for line in data:
        hand_str, bid = line.split()
        poker_hands.append((compute_hand_value(hand_str), int(bid)))
    poker_hands.sort()

    part1 = sum((rank+1) * hand[1] for rank, hand in enumerate(poker_hands))
    print(f"Part 1: {part1}")
