#!/usr/bin/env python3

import os.path

def find_captcha(number, offset=1):
    """Find the sum of digits such that number[i] = number[(i+offset) % n]"""

    s = 0
    n = len(number)
    for i in range(n):
        if number[i] == number[(i+offset) % n]:
            s += int(number[i])

    return s

if __name__ == '__main__':
    filename = "day01_captcha.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        number = open(filename).read().strip()
        part_1 = find_captcha(number)
        print("PART ONE:", part_1)
        part_2 = find_captcha(number, offset=len(number)//2)
        print("PART TWO:", part_2)

