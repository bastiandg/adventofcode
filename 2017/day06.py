#!/usr/bin/env python3

input = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
memory_bank = [int(i) for i in input.split("\t")]
length = len(memory_bank)

past_banks = []
while memory_bank not in past_banks:
    past_banks.append(list(memory_bank))
    max_block = 0
    max_index = 0
    for i in range(length):
        if memory_bank[i] > max_block:
            max_block = memory_bank[i]
            max_index = i
    memory_bank[max_index] = 0
    j = max_index
    for i in range(max_block):
        memory_bank[(max_index + i + 1) % length] += 1

print(len(past_banks))
print(len(past_banks) - past_banks.index(memory_bank))
