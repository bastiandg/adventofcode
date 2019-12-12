#!/usr/bin/env python3
import sys
# import string
input = open("day02.in", "r").read().split("\n")[:-1]

doubleLineCount = 0
tripleLineCount = 0

for line in input:
    charset = set(line)
    doubleCounted = False
    tripleCounted = False
    for char in charset:
        if line.count(char) == 2 and not doubleCounted:
            doubleLineCount += 1
            doubleCounted = True
        if line.count(char) == 3 and not tripleCounted:
            tripleLineCount += 1
            tripleCounted = True
print(doubleLineCount * tripleLineCount)

l = len(input[0])
for i in range(len(input)):
    for j in range(i, len(input)):
        commonCount = 0
        for c in range(l):
            if input[i][c] == input[j][c]:
                commonCount += 1
        if commonCount == l - 1:
            print(input[i])
            print(input[j])
            sys.exit()
