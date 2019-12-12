#!/usr/bin/env python3

input = open("day12.txt", "r").read().split("\n")[:-1]

pipes = [set([int(number) for number in line.replace(" <->", "").replace(",", "").split(" ")]) for line in input]

updated = True
while updated:
    updated = False
    for i in range(len(pipes)):
        if i == len(pipes) - 1:
            break
        for j in range(i, len(pipes)):
            if i != j and len(pipes[i].intersection(pipes[j])) > 0:
                pipes[i].update(pipes[j])
                del(pipes[j])
                updated = True
                break
        if updated:
            break

print(len(pipes[0]))
print(len(pipes))
