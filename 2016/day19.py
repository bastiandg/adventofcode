#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

for input in range(4, 243):
    elves = [1] * input
    position = 0
    for i in range(input - 1):
        length = input - i
        jump =  math.floor(length / 2)
        jumpPosition = position
        while jump > 0:
            jump -= elves[jumpPosition]
            jumpPosition = (jumpPosition + 1) % input
        while elves[jumpPosition] == 0:
            jumpPosition = (jumpPosition + 1) % input
        elves[jumpPosition] = 0
        position = (position + 1) % input
        while elves[position] == 0:
            position = (position + 1) % input
    n = input
    x = elves.index(1) + 1
    l = math.floor(math.log(n, 3))
    f = n - 3 ** l + ((n // (3 ** l) + 1) % 2) * (n - (3 ** l) * 2)

    print("%i %i %i" % (n, x, f))

n = 3014603
l = math.floor(math.log(n, 3))
f = n - 3 ** l + ((n // (3 ** l) + 1) % 2) * (n - (3 ** l) * 2)
print(f)
