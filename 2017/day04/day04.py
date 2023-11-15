#!/usr/bin/env python3

import os.path

def number_valid(passphrases):
    """Return the number of valid passphrase (tuple) if:
         - all words must be different (part 1)
         - no words should be anagrams (part 2)
    """

    n_valid_1 = n_valid_2 = 0
    for passphrase in passphrases:
        words = passphrase.split()
        sorted_words = [''.join(sorted(w)) for w in words]

        if len(set(words)) == len(words):
            n_valid_1 += 1
        if len(set(sorted_words)) == len(words):
            n_valid_2 += 1

    return n_valid_1, n_valid_2

if __name__ == '__main__':
    filename = "day04_passphrases.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        passphrases = open(filename).read().strip().split("\n")
        part_1, part_2 = number_valid(passphrases)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
