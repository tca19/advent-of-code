#!/usr/bin/env python3

import re
import os.path

def score(stream):
    """Compute the score of stream and length of garbage in stream."""

    # remove canceled characters
    stream = re.sub("!.", "", stream)

    # get length of garbage
    garbage = re.findall("<(.*?)>", stream)
    garbage_length = len("".join(garbage))

    # remove garbage
    stream = re.sub("<.*?>", "", stream)

    # score is increased for every new group (occurs with opening { ). For every
    # new group, depth is incremented by 1
    score = 0
    depth = 0
    for c in stream:
        if c == "{":
            depth += 1
            score += depth
        elif c == "}":
            depth -= 1

    return score, garbage_length

if __name__ == '__main__':
    filename = "day09_stream.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        stream = open(filename).read().strip()
        part_1, part_2 = score(stream)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
