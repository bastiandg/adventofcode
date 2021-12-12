#!/usr/bin/python3

input = [int(i) for i in open("day01.txt", "r").read().split("\n")[:-1]]
increments = 0
windowIncrements = 0

for i in range(len(input) - 1):
    if input[i + 1] > input[i]:
        increments += 1

for i in range(len(input) - 3):
    if sum(input[i + 1:i + 4]) > sum(input[i:i + 3]):
        windowIncrements += 1

print(increments)
print(windowIncrements)
