#!/usr/bin/env python3

input = open("day02.txt", "r").read().split("\n")[:-1]
s1 = 0
s2 = 0

for line in input:
    numbers = [int(x) for x in line.split("\t")]
    s1 += max(numbers) - min(numbers)
    length = len(numbers)
    for n1 in numbers:
        for n2 in numbers:
            if n1 != n2 and (n1 % n2) == 0:
                s2 += n1 // n2

print(s1)
print(s2)
