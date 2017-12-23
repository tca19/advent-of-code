#!/usr/bin/env python3

def day23():
    a = 1
    b = 100000 + 93*100
    c = b + 17000
    f = 0
    while b-c:
        for d in range(2,b+1):
            if b%d == 0:
                if 2 <= b//d <= b:
                    f += 1
                    break
        b += 17
    for d in range(2,b+1):
        if b%d == 0:
            if 2 <= b//d <= b:
                f += 1
                break
    print(f)

day23()
