#!/usr/bin/python3

import sys
input = open("day01.txt", "r").read().split("\n")[:-1]

sum = 2020
entries = set()

for line in input:
    entries.add(int(line))

for entry in entries:
    if (sum - entry) in entries:
        print(entry * (sum - entry))
        break

sortedEntries = sorted(entries)

for i in range(len(sortedEntries)):
    for j in range(i + 1, len(sortedEntries)):
        if (sum - sortedEntries[i] - sortedEntries[j]) in entries:
            print(sortedEntries[i] * sortedEntries[j] * (sum - sortedEntries[i] - sortedEntries[j]))
            sys.exit(0)
