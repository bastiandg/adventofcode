#!/usr/bin/env python3

input = open("day05.txt", "r").read().split("\n")[:-1]

jump_list = [int(line) for line in input]
jump_list2 = list(jump_list)
length = len(jump_list)

position = 0
step_counter = 0

while True:
    ptmp = position
    try:
        position += jump_list[position]
    except IndexError:
        break
    jump_list[ptmp] += 1
    step_counter += 1
print(step_counter)

step_counter = 0
position = 0
while True:
    ptmp = position
    try:
        position += jump_list2[position]
    except IndexError:
        break
    if jump_list2[ptmp] < 3:
        jump_list2[ptmp] += 1
    else:
        jump_list2[ptmp] -= 1
    step_counter += 1
print(step_counter)
