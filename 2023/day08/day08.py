#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Python3 solution for the problem of Day 8 in Advent of Code 2023.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# We are given a file that contains instructions to build a graph and
# instructions to navigate through it. An example of such file is:
#
#   RL
#
#   AAA = (BBB, CCC)
#   BBB = (DDD, EEE)
#   CCC = (ZZZ, GGG)
#   DDD = (DDD, DDD)
#   EEE = (EEE, EEE)
#   GGG = (GGG, GGG)
#   ZZZ = (ZZZ, ZZZ)
#
# The first line (RL in this case) represents instructions to navigate through
# the graph. We always start at the node AAA and then follow the instructions.
# First letter is 'R'. It means "right" so we have to go to the right direction
# from AAA. Second letter is 'L'. It means "left" so we have to go to the left
# direction then. And after? We repeat the navigation instructions until we
# reach the node ZZZ (final node of our traversal).
#
# The others lines describe the structure of the graph. Each line indicates a
# node and the possible choices we have to go next (first choice is named
# "left", second choice is named "right"). Each choice leads to another node in
# the graph. For example, with the line "AAA = (BBB, CCC)", it means that from
# AAA, if we choose "left" we go to BBB; if we choose "right" we go to CCC.
#
# Part 1
# ======
# Traverse the graph following the provided left/right instructions, starting
# from node AAA until you reach node ZZZ. The task is to find how many steps
# does it need to go from AAA to ZZZ.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import argparse
from itertools import cycle


def build_graph(lines: str) -> dict:
    """
    Return a graph structure created by the given instructions `lines`.
        Parameters:
            lines (str): A long string composed of several lines. Each line is
                         separated by a "\n".

        Returns:
            graph (dict): The graph structure, as a dictionary. Eack key is a
                          node and its values are the possible choices
                          (= neighbors) from this node.
    """
    graph = {}

    for line in lines.split("\n"):
        # Each line is like: AAA = (BBB, CCC)
        node, choices = line.split(" = ")
        choices = choices.strip()[1:-1]  # remove the '(' and ')'
        left, right = choices.split(", ")
        graph[node] = {"left": left, "right": right}
    return graph


def traverse_graph(graph: dict, instructions: str) -> int:
    """
    Return the number of steps required to traverse the graph from AAA to ZZZ
    following the given `instructions`.

        Parameters:
            graph (dict): The graph structure to traverse.
            instructions (string): The instructions used to traverse the graph.
                                   A string composed of "L" and "R" characters,
                                   indicating if we need to go "left" or
                                   "right" to reach the next node.

        Returns:
            n_steps (int): The number of steps required to reach the node ZZZ
                           starting from node AAA.
    """
    n_steps = 0
    current = "AAA"
    finish = "ZZZ"

    for instruction in cycle(instructions):
        if current == finish:
            break
        choice = "left" if instruction == "L" else "right"
        current = graph[current][choice]
        n_steps += 1

    return n_steps


if __name__ == "__main__":
    # pylint: disable=C0103
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Filename of your input file.",
                        default="day08.input")
    args = parser.parse_args()

    # We open the input file, and read it block by block.
    with open(args.input, encoding="UTF-8") as f:
        traverse_instructions, graph_instructions = f.read().split("\n\n")

    G = build_graph(graph_instructions.strip())
    part1 = traverse_graph(G, traverse_instructions)
    print(f"Part 1: {part1}")
