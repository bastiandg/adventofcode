#!/usr/bin/env python3

import copy

input = open("day13.txt", "r").read().split("\n")[:-1]
scanner_lengths = [-1] * 97
scanner_positions = [-1] * 97
firewall_length = len(scanner_lengths)


def print_scanners():
    print()
    for i in range(firewall_length):
        if scanner_positions[i] != -1:
            print("%i: %i" % (i, scanner_positions[i][0]))


def move_scanners():
    for i in range(firewall_length):
        if scanner_positions[i] != -1:
            if scanner_positions[i][0] + scanner_positions[i][1] == scanner_lengths[i]:
                scanner_positions[i][1] = -1
            elif scanner_positions[i][0] + scanner_positions[i][1] == -1:
                scanner_positions[i][1] = 1
            scanner_positions[i][0] += scanner_positions[i][1]


def reset_scanners():
    for line in input:
        line_split = line.split(":")
        scanner_index = int(line_split[0])
        scanner_positions[scanner_index] = [0, 1]
        scanner_length = int(line_split[1])
        scanner_lengths[scanner_index] = scanner_length


reset_scanners()

caught = 0
for j in range(firewall_length):
    if scanner_positions[j] != -1 and scanner_positions[j][0] == 0:
        caught += scanner_lengths[j] * j
    move_scanners()
print(caught)


tmp_scanner_positions = copy.deepcopy(scanner_positions)
max_steps = 0
passed = False
stalled_steps = 0

while not passed:
    caught = False
    scanner_positions = copy.deepcopy(tmp_scanner_positions)
    move_scanners()
    tmp_scanner_positions = copy.deepcopy(scanner_positions)
    for j in range(firewall_length):
        if scanner_positions[j] != -1 and scanner_positions[j][0] == 0:
            caught = True
            reset_scanners()
            stalled_steps += 1
            if j > max_steps:
                max_steps = j
                print("steps: %i" % j)
                print("stalled_steps: %i" % (stalled_steps - 1))
            break
        for i in range(firewall_length):
            move_scanners()
    if not caught:
        passed = True
print(stalled_steps)
