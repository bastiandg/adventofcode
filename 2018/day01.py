#!/usr/bin/env python3
import sys
input = open("day01.in", "r").read().split("\n")[:-1]

s = 0
for line in input:
    s += int(line)
print(s)

s = 0
sd = set()
while True:
    for line in input:
        if s in sd:
            print(s)
            sys.exit()

        else:
            sd.add(s)
        s += int(line)

