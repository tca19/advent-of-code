#!/usr/bin/env python3


import os.path
s = 0

def checksum_rows(lines):
    """Compute the checksum (max - min) for each row. Sum all checksums."""

    s = 0
    for line in lines:
        row = list(map(int, line.split()))
        s += max(row) - min(row)

    return s

def evenly_divide_rows(lines):
    """Find the two numbers of each row where one evenly divide the other. Sum
    the results of all divisions."""

    s = 0

    for line in lines:
        row = list(map(int, line.split()))
        n = len(row)
        for i in range(n-1):
            for j in range(i+1, n):
                if row[i] % row[j] == 0:
                    s += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    s += row[j] // row[i]

    return s

if __name__ == '__main__':
    filename = "day02_spreadsheet.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lines = open(filename).read().strip().split("\n")
        part_1 = checksum_rows(lines)
        print("PART ONE:", part_1)
        part_2 = evenly_divide_rows(lines)
        print("PART TWO:", part_2)
