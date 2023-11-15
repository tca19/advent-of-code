#!/usr/bin/env python3

def value_after_2017(step):
    """Generate the circular buffer according to the rule. Return value next to
    2017."""

    buf, pos = [0], 0

    # i is current length of circular buffer. If i=10 then the buffer
    # contains number from 0 to 9, so the value inserted is 10 (that's i).
    for i in range(1, 2018):
        pos = (pos+step) % i
        buf = buf[:pos+1] + [i] + buf[pos+1:]
        pos += 1

    return buf[pos+1]

def value_after_0(step):
    """Return the value next to 0 if we insert 50M new items in circular
    buffer."""

    pos, ans = 0, -1

    # it is impossible that a new value is inserted before 0, so it means that 0
    # will always be at position 0. We only care of the value next to it. This
    # value change only when we insert a new element directly after 0 i.e. when
    # the current position after moving forward is 0.
    for i in range(1, 50000001):
        pos = (pos+step) % i

        if pos == 0:
            ans = i

        pos += 1

    return ans

if __name__ == '__main__':
    step = 371
    part_1 = value_after_2017(step)
    print("PART ONE:", part_1)
    part_2 = value_after_0(step)
    print("PART TWO:", part_2)
