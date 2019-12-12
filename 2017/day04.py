#!/usr/bin/env python3

input = open("day04.txt", "r").read().split("\n")[:-1]
valid_passwords = 0
valid_passwords2 = 0

for line in input:
    words = line.split()
    if len(set(words)) == len(words):
        valid_passwords += 1

for line in input:
    words = ["".join(sorted(w)) for w in line.split()]
    if len(set(words)) == len(words):
        valid_passwords2 += 1

print(valid_passwords)
print(valid_passwords2)
